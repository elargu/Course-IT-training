<?php
$aErrores=array();
$recupera=array();
$criptoreturn=array();
$conexion="";
$retorno=array();
//por alguna razon este patron me toma valido el simbolo ? no se como sacarlo
$patron_usuario = "/^[a-zA-Z0123456789ñÑáéíóúÁÉÍÓÚ\s]+$/";

//*************************************FUNCIONES*****************************************************************
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

//*****************************************main*************************************************************
//1)Chequeo los datos ingresados si son caracteres validos

$varchk="".$_POST['user_log']."";
$txtTMA=5;
$txtTMB=10;
$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='nombre usuario: '.$recupera[1];};
//chequeo password
$varchk="".$_POST['pass_log']."";
$txtTMA=5;
$txtTMB=10;
$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='password: '.$recupera[1];};

//muestro los errores si los hay
$existe_error=false;
$tamErr=sizeof($aErrores);
if($tamErr>0){
	Echo"Se han encontrado los siguientes errores<br/>";
	$existe_error=true;
	foreach($aErrores as $error){
		echo $error."<br/>";
	};
	echo "<p><a href='index_login.html'>Haz clic aquí para volver al formulario</a></p>";
}else{
	$existe_error=false;
};

//si no hay errores proceso a habilitar el logueo, corroboro usuario y contraseña
if($existe_error==false){
	//encripto la clave en md5 y la guardo en la variable $passencrip
	$criptoreturn= encriptar_txt($_POST['pass_log']);
	if($criptoreturn[0]=='1'){$passencrip=$criptoreturn[1];};

	//VAMOS A COMPROBAR EXISTE EL USUARIO SELECCIONADO Y SU CORRESPONDIENTE PASSWORD.
	//en un array, devuelvo a traves de la funcion "on_table()" el mysqli_connect y el mysqli_connect_errno. Qudando en posicion 0 y 1 respectivamente.Inicio la conexion con la base de datos.
	$retorno=on_table();
	//aca le paso el mysqli_connect a la variable $conexion.
	$conexion=$retorno[0];
	if (!$retorno[1]){
		$querydata="Select * from usuarios where nombre_usuario = '".$_POST['user_log']."';";
		$status=orden_ejecute($conexion,$querydata);
		if($status){
			$fila = mysqli_fetch_row($status);
			if($fila){
					if($fila[2]==$passencrip){
						echo"<br/>logueo correcto!<br/><br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para continuar con la sesion en el menu de usuario</a></p>";
					}else{
						echo"<br/>contraseña incorrecta<br/><br/>";echo "<p><a href='index_login.html'>Haz clic aquí para intentar de nuevo</a></p>";
					};				
			}else{echo "usuario no existe<br/>";echo "<p><a href='index_login.html'>Haz clic aquí para intentar de nuevo</a></p>";};
		};
	}else{echo"fallo conexio base de datos 1er intento";};
	//cerramos conexion
	off_table($conexion);
}

?>