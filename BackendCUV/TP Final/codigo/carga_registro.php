<?php

$aErrores=array();
$aMensajes=array();
$recupera=array();
$criptoreturn=array();
$conexion="";
$retorno=array();
$patron_texto = "/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/";
//por alguna razon este patron me toma valido el simbolo ? no se como sacarlo
$patron_usuario = "/^[a-zA-Z0123456789ñÑáéíóúÁÉÍÓÚ\s]+$/";

//la funcion chk_patron() sirve para revisar si los datos ingresados corresponden al criterio del patron
function chk_patron($txt,$pat,$na,$nb){
	$msj=array();
	if(empty($txt)){
		$msj[0]='1';$msj[1]='[Debe especificar parametro]';
	}else{
		if(!preg_match($pat,$txt)){
			$msj[0]='1';$msj[1]='[caracteres no validos]';
		}else{
			if((strlen($txt)<$na)||(strlen($txt)>$nb)){
				$msj[0]='1';$msj[1]='[el tamaño del texto no corresponde con el criterio solicitado]';
			;}else{
				$msj[0]='0';$msj[1]="[".$txt."]";
			};
		};
	};
	return $msj;
};

//la funcion encriptar_txt() sirve para encriptar en md5 la clave ingresada
function encriptar_txt($miclave){
	$encr=array();
	if( CRYPT_MD5 == 1 ){
		$encr[0]="1";$encr[1]="".crypt($miclave,'$1$holacomo894o$')."";
	}else{
		$encr[0]="0";
		echo "Hash MD5 no soportado o error<p />";
	};
	return $encr;
};


//la funcion "on_table()" es para habilitar la conexion con la base de datos
function on_table(){
	$conext = mysqli_connect( "localhost", "root", "", "ejercicio_final");
	if (mysqli_connect_errno()){printf("Falló la conexión: %s\n", mysqli_connect_error());}
	return $ar_on=array($conext,mysqli_connect_errno());
};
//la funcion "off_table()" es para cerrar la conexion con la base de datos
function off_table($conext){
	mysqli_close($conext);
};

//la funcion "orden_ejecute()" ejecuta el query
function orden_ejecute($conext,$querydt){
	$sql = $querydt;
	$rs = mysqli_query($conext, $sql);
	return $rs;
}






//CHEQUEO DATOS INGRESADOS
//Para: nombre de Usuario, Contraseña, Nombre y Apellido voy a utilizar la funcion chk_patron() que me permite corroborar una serie de caracteristicas. Se le tendra que pasar la variable del formulario, el patron de comparacion y el tamaño minimo y maximo del dato aceptado ingresado en el formulario.
//Para: Edad y Sexo, utilize un if aparte porque no tenia similitudes con los otros datos.
//en $varchek vamos a mandar el texto que el usuario entro en el formulario y vamos a chequearlo que cumpla las condiciones. $txtTMA y $txtTMB es el tamaño que puede tener, tanto minimo y maximo respectivamente.

//chequeo nombre de usuario
$varchk="".$_POST['txt_newusuario']."";
$txtTMA=5;
$txtTMB=10;
$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='nombre usuario: '.$recupera[1];}else{$aMensajes[]='nombre usuario: '.$recupera[1];};
//chequeo password
$varchk="".$_POST['txt_newpassword']."";
$txtTMA=5;
$txtTMB=10;
$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='password: '.$recupera[1];}else{$aMensajes[]='password: '.$recupera[1];};
//chequeo nombre
$varchk="".$_POST['txt_newnombre']."";
$txtTMA=1;
$txtTMB=24;
$recupera=chk_patron($varchk,$patron_texto,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='nombre: '.$recupera[1];}else{$aMensajes[]='nombre: '.$recupera[1];};
//chequeo apellido
$varchk="".$_POST['txt_newapellido']."";
$txtTMA=1;
$txtTMB=24;
$recupera=chk_patron($varchk,$patron_texto,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='apellido: '.$recupera[1];}else{$aMensajes[]='apellido: '.$recupera[1];};

//chequeo edad
if(!empty($_POST['num_newedad'])){
	if(is_numeric($_POST['num_newedad'])){
		if(($_POST['num_newedad'])>0){
			$aMensajes[]='edad: '.$_POST['num_newedad'];
		}else{
			$aErrores[]='edad: [La edad tiene que ser mayor a cero]';
		};
	}else{
		$aErrores[]='edad: [El dato ingresado tiene que ser numerico]';
	};
}else{
	$aErrores[]='edad: [Debe especificar parametro]';
};

//chequeo sexo
if(!empty($_POST['sel_newsex'])){
	if(($_POST['sel_newsex']=='Hombre')||($_POST['sel_newsex']=='Mujer')||($_POST['sel_newsex']=='Otro')){
		$aMensajes[]='Sexo :'.$_POST['sel_newsex'];
	}else{
		$aErrores[]="Sexo : La opcion no es valida";
	};
}else{
	$aErrores[]="Sexo : No ingreso ninguna opcion";
};


//muestro el resultado en la pantalla o lo errores si los hay
$tamErr=sizeof($aErrores);
if($tamErr>0){
	Echo"Se han encontrado los siguientes errores<br/>";
	foreach($aErrores as $error){
		echo $error."<br/>";
	};
	echo "<p><a href='carga_registro.html'>Haz clic aquí para volver al formulario</a></p>";
}else{
	$i=0;
	foreach($aMensajes as $msj){
		if($i!=1){echo $msj."<br/>";};
		$i++;
	};
};




//VAMOS A COMPROBAR SI NO EXISTE EL USUARIO SELECCIONADO. creamos un flag:
$flagusr=false;
//en un array, devuelvo a traves de la funcion "on_table()" el mysqli_connect y el mysqli_connect_errno. Qudando en posicion 0 y 1 respectivamente.Inicio la conexion con la base de datos.
$retorno=on_table();
//aca le paso el mysqli_connect a la variable $conexion.
$conexion=$retorno[0];
if (!$retorno[1]){
	$querydata="Select * from usuarios where nombre_usuario = '".$_POST['txt_newusuario']."';";
	$status=orden_ejecute($conexion,$querydata);
	if($status){
		$fila = mysqli_fetch_row($status);
		if($fila){
				$flagusr=true;
				echo"<br/>-nombre de Usuario: Existe un usuario con ese nombre! Elija otro.<br/>No se guardaron los datos.<br/><br/>";
				echo "<p><a href='carga_registro.html'>Haz clic aquí para volver al formulario</a></p>";
		}else{$flagusr=false;};
	};
}else{echo"fallo conexio base de datos 1er intento";};
//cerramos conexion
off_table($conexion);



//encripto la clave
$criptoreturn= encriptar_txt($_POST['txt_newpassword']);
if($criptoreturn[0]=='1'){$passencrip=$criptoreturn[1];};

//guardo los datos si se pudo encriptar la clave y si no hubo errores en la carga del formulario
if(($criptoreturn[0]=='1')&&($tamErr==0)&&($flagusr==false)){
	
	//en un array, devuelvo a traves de la funcion "on_table()" el mysqli_connect y el mysqli_connect_errno. Qudando en posicion 0 y 1 respectivamente.Inicio la conexion con la base de datos.
	$retorno=on_table();
	//aca le paso el mysqli_connect a la variable $conexion.
	$conexion=$retorno[0];
	
	//si mysqli_connect_errno es falso (o sea no hubo errores) se procede a ejecutar
	if (!$retorno[1]){
		$querydata="SELECT * FROM usuarios ORDER BY id_usuario;";
		//se ejuta el query
		$status=orden_ejecute($conexion,$querydata);
		//con este if traigo cual es el ultimo id cargado en la base de datos
		if($status){
			$posicion = mysqli_num_rows($status);
			$posicion = $posicion-1;
			if(mysqli_data_seek($status,$posicion)){
				$fila=mysqli_fetch_row($status);
				$idultimo=$fila[0];
				$idnew=$idultimo+1;
				mysqli_free_result($status);
			}else{echo"error en el salto;";};
		}else{echo"Error al listar tabla";};
		
		//echo "$idnew<br/>";
		
		//cargo los datos a la base de datos mysql
		$querydata="INSERT INTO usuarios VALUES (".$idnew.",'".$_POST['txt_newusuario']."','".$passencrip."','".$_POST['txt_newnombre']."','".$_POST['txt_newapellido']."',".$_POST['num_newedad'].",'".$_POST['sel_newsex']."');";
		$status=orden_ejecute($conexion,$querydata);
		if($status){
			echo"los datos han sido cargado con exito!<br/>";
			echo "<p><a href='index_login.html'>Haz clic aquí para volver a la pantalla login</a></p>";
		}else{echo"Error cargar datos a la tabla";};	
	};
	//cerramos conexion
	off_table($conexion);
};

?>