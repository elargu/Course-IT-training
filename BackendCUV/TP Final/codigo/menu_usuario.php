<?php

$aErrores=array();
$aMensajes=array();
$recupera=array();
$criptoreturn=array();
$newcriptoreturn=array();
$conexion="";
$logeo_correcto=false;
$radio_correcto=false;
$retorno=array();
$patron_texto = "/^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/";
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


//////////////////////basicamente es misma que index_login.php (por mis escasos conocimiento de html no se como unificar esos critoerios para que quede todo en uno)/////////////
//1)Chequeo los datos ingresados si son caracteres validos
$varchk="".$_POST['txt_usuario']."";
$txtTMA=5;
$txtTMB=10;
$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
if($recupera[0]=='1'){$aErrores[]='nombre usuario: '.$recupera[1];};
//chequeo password
$varchk="".$_POST['txt_usrpassword']."";
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
	echo "<p><a href='menu_usuario.html'>Haz clic aquí para volver al formulario</a></p>";
}else{
	$existe_error=false;
};

//si no hay errores proceso a habilitar el logueo, corroboro usuario y contraseña
if($existe_error==false){
	//encripto la clave en md5 y la guardo en la variable $passencrip
	$criptoreturn= encriptar_txt($_POST['txt_usrpassword']);
	if($criptoreturn[0]=='1'){$passencrip=$criptoreturn[1];};

	//VAMOS A COMPROBAR EXISTE EL USUARIO SELECCIONADO Y SU CORRESPONDIENTE PASSWORD.
	//en un array, devuelvo a traves de la funcion "on_table()" el mysqli_connect y el mysqli_connect_errno. Qudando en posicion 0 y 1 respectivamente.Inicio la conexion con la base de datos.
	$retorno=on_table();
	//aca le paso el mysqli_connect a la variable $conexion.
	$conexion=$retorno[0];
	if (!$retorno[1]){
		$querydata="Select * from usuarios where nombre_usuario = '".$_POST['txt_usuario']."';";
		$status=orden_ejecute($conexion,$querydata);
		if($status){
			$fila = mysqli_fetch_row($status);
			if($fila){
					if($fila[2]==$passencrip){
							$logeo_correcto=true;
					}else{
						echo"<br/>contraseña incorrecta<br/><br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";
					};				
			}else{echo "usuario no existe<br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};
		};
	}else{echo"fallo conexio base de datos 1er intento";};
	//cerramos conexion
	off_table($conexion);
}

//////////////////////////////////////////////

//si esta el boton radio "menu_opcion" lleno activo la vandera $radio_correcto, en caso contrario saco un aviso;
if(!empty($_POST['menu_opcion'])){$radio_correcto=true;}else{echo"No selecciono opcion si va a modificar o borrar la cuenta, selecione 'modificar' o 'borrar' o puede salir del menu<br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};


if(($radio_correcto==true)&&($logeo_correcto==true)){
	
	$fningun_err=true;
	
	$seleccion_opc="".$_POST['menu_opcion']."";
	switch($seleccion_opc){
		
		case"modificar":
		
			$flag_casillavacia=false;
			if((empty($_POST['txt_modpassword']))&&(empty($_POST['txt_modnombre']))&&(empty($_POST['txt_modapellido']))&&(empty($_POST['num_modedad']))&&(empty($_POST['sel_modsex']))){echo"No ingreso ninguna opcion, seleccione para modificar<br/>";echo"<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";$flag_casillavacia=true;};

			if($flag_casillavacia==false){
				
				if(!empty($_POST['txt_modpassword'])){
					//chequeo password
					$varchk="".$_POST['txt_modpassword']."";
					$txtTMA=5;
					$txtTMB=10;
					$recupera=chk_patron($varchk,$patron_usuario,$txtTMA,$txtTMB);
					if($recupera[0]=='1'){$aErrores[]='password: '.$recupera[1];$fningun_err=false;}else{$aMensajes[]='password: '.$recupera[1];};
				}
			
				if(!empty($_POST['txt_modnombre'])){
					//chequeo nombre
					$varchk="".$_POST['txt_modnombre']."";
					$txtTMA=1;
					$txtTMB=24;
					$recupera=chk_patron($varchk,$patron_texto,$txtTMA,$txtTMB);
					if($recupera[0]=='1'){$aErrores[]='nombre: '.$recupera[1];$fningun_err=false;}else{$aMensajes[]='nombre: '.$recupera[1];};
				}
			
				if(!empty($_POST['txt_modapellido'])){
					//chequeo apelido
					$varchk="".$_POST['txt_modapellido']."";
					$txtTMA=1;
					$txtTMB=24;
					$recupera=chk_patron($varchk,$patron_texto,$txtTMA,$txtTMB);
					if($recupera[0]=='1'){$aErrores[]='apellido: '.$recupera[1];$fningun_err=false;}else{$aMensajes[]='apellido: '.$recupera[1];};
				}
		
		
				//chequeo edad
				if(!empty($_POST['num_modedad'])){
					if(is_numeric($_POST['num_modedad'])){
						if(($_POST['num_modedad'])>0){$aMensajes[]='edad: '.$_POST['num_modedad'];
						}else{$aErrores[]='edad: [La edad tiene que ser mayor a cero]';$fningun_err=false;};
					}else{$aErrores[]='edad: [El dato ingresado tiene que ser numerico]';$fningun_err=false;};
				}

				//chequeo sexo
				if(!empty($_POST['sel_modsex'])){
					if(($_POST['sel_modsex']=='Hombre')||($_POST['sel_modsex']=='Mujer')||($_POST['sel_modsex']=='Otro')){$aMensajes[]='Sexo :'.$_POST['sel_modsex'];
					}else{$aErrores[]="Sexo : La opcion no es valida";$fningun_err=false;};
				}
		
				//Si hay errores los muestro en pantalla y le pido al usuario que vuelva al formulario a correigrlo
				if($fningun_err==false){
					echo"Se cometieron los siguientes errores y no se guardaron los cambios:<br/>";
						foreach($aErrores as $error){
							echo $error."<br/>";
						};
					echo "<p><a href='menu_usuario.html'>Haz clic aquí para volver al formulario</a></p>";
				}else{
				
				
					//Informe de la actualizacion de la base de datos, informacion de la base.
					$retorno=on_table();
					$conexion=$retorno[0];
					if (!$retorno[1]){
						$querydata="Select * from usuarios where nombre_usuario = '".$_POST['txt_usuario']."';";
						$status=orden_ejecute($conexion,$querydata);
						if($status){
							$fila = mysqli_fetch_row($status);
							if($fila){
							
								echo"<br/><br/><br/>";
								echo"<br/>***************************************************<br/>";
								echo"Informacion Antigua de la base de datos<br/>";
								echo"<br/>___________________________________________________<br/>";
								echo"Usuario:".$fila[1]."<br/>";
								echo"Nombre:".$fila[3]."<br/>";
								echo"Apellido:".$fila[4]."<br/>";
								echo"Edad:".$fila[5]."<br/>";
								echo"Sexo:".$fila[6]."<br/>";
								echo"<br/>___________________________________________________<br/>";
								echo"El password no se vera en este informe<br/>";
								echo"<br/><br/><br/>";
							
							}else{echo "usuario no existe<br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};};
					}else{echo"fallo conexio base de datos 1er intento";};
					//cerramos conexion
					off_table($conexion);
								
				
					//en un array, devuelvo a traves de la funcion "on_table()" el mysqli_connect y el mysqli_connect_errno. Qudando en posicion 0 y 1 respectivamente.Inicio la conexion con la base de datos.
					$retorno=on_table();
					//aca le paso el mysqli_connect a la variable $conexion.
					$conexion=$retorno[0];
					if (!$retorno[1]){
							
							if(!empty($_POST['txt_modpassword'])){
								//encripto la clave en md5 y la guardo en la variable $passencrip
								$newcriptoreturn= encriptar_txt($_POST['txt_modpassword']);
								if($newcriptoreturn[0]=='1'){$newpassencrip=$newcriptoreturn[1];};
								//armo el queri y envio a ejecutar el cambio
								$querydata="UPDATE usuarios SET password_usr='".$newpassencrip."' WHERE nombre_usuario='".$_POST['txt_usuario']."';";
								$status=orden_ejecute($conexion,$querydata);
								//imprimo el resultado de la ejecucion
								if($fila){echo"password cambiado con exito<br/>";}else{echo"error al actualizar password, no se guardo cambio<br/>";};
							};
						
							if(!empty($_POST['txt_modnombre'])){
								//armo el queri y envio a ejecutar el cambio
								$querydata="UPDATE usuarios SET dato_nombre='".$_POST['txt_modnombre']."' WHERE nombre_usuario='".$_POST['txt_usuario']."';";
								$status=orden_ejecute($conexion,$querydata);
								if($fila){echo"nombre cambiado con exito<br/>";}else{echo"error al actualizar nombre, no se guardo cambio<br/>";};
							};
						
							if(!empty($_POST['txt_modapellido'])){
								//armo el queri y envio a ejecutar el cambio
								$querydata="UPDATE usuarios SET dato_apellido='".$_POST['txt_modapellido']."' WHERE nombre_usuario='".$_POST['txt_usuario']."';";
								$status=orden_ejecute($conexion,$querydata);
								if($fila){echo"apellido cambiado con exito<br/>";}else{echo"error al actualizar apellido, no se guardo cambio<br/>";};
							};
						
							if(!empty($_POST['num_modedad'])){
								//armo el queri y envio a ejecutar el cambio
								$querydata="UPDATE usuarios SET dato_edad=".$_POST['num_modedad']." WHERE nombre_usuario='".$_POST['txt_usuario']."';";
								$status=orden_ejecute($conexion,$querydata);
								if($fila){echo"edad cambiado con exito<br/>";}else{echo"error al actualizar edad, no se guardo cambio<br/>";};
							};
						
						
							if(!empty($_POST['sel_modsex'])){
								//armo el queri y envio a ejecutar el cambio
								$querydata="UPDATE usuarios SET dato_sexo='".$_POST['sel_modsex']."' WHERE nombre_usuario='".$_POST['txt_usuario']."';";
								$status=orden_ejecute($conexion,$querydata);
								if($fila){echo"sexo cambiado con exito<br/>";}else{echo"error al actualizar sexo, no se guardo cambio<br/>";};
							};
						
					}else{echo"fallo conexio base de datos 1er intento";};
					//cerramos conexion
					off_table($conexion);
				
					//Informe de la actualizacion de la base de datos, informacion de la base.
					$retorno=on_table();
					$conexion=$retorno[0];
					if (!$retorno[1]){
						$querydata="Select * from usuarios where nombre_usuario = '".$_POST['txt_usuario']."';";
						$status=orden_ejecute($conexion,$querydata);
						if($status){
							$fila = mysqli_fetch_row($status);
							if($fila){
							
								echo"<br/>***************************************************<br/>";
								echo"Informacion actualizada de la base de datos<br/>";
								echo"<br/>___________________________________________________<br/>";
								echo"Usuario:".$fila[1]."<br/>";
								echo"Nombre:".$fila[3]."<br/>";
								echo"Apellido:".$fila[4]."<br/>";
								echo"Edad:".$fila[5]."<br/>";
								echo"Sexo:".$fila[6]."<br/>";
								echo"<br/>___________________________________________________<br/>";
								echo"si usted modifico password no se vera el dato en este informe<br/>";
								echo"<br/>***************************************************<br/>";
							
							}else{echo "usuario no existe<br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};};
					}else{echo"fallo conexio base de datos 1er intento";};
					//cerramos conexion
					off_table($conexion);
				
					echo "<p><a href='menu_usuario.html'>Haz clic aquí para volver al menu usuario</a></p>";
				};
			};
		
			break;
		case"borrar":
		
			$retorno=on_table();
			$conexion=$retorno[0];
			if (!$retorno[1]){
				$querydata="DELETE FROM usuarios WHERE nombre_usuario = '".$_POST['txt_usuario']."';";
				$status=orden_ejecute($conexion,$querydata);
				if($status){
					$querydata="Select * from usuarios where nombre_usuario = '".$_POST['txt_usuario']."';";
					$status=orden_ejecute($conexion,$querydata);
					if($status){echo"El usuario a sido borrado con exito!";echo "<p><a href='index_login.html'>Haz clic aquí para volver a pantalla de logeo</a></p>";}else{echo"No pudo borrase el usuario.";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};
				}else{echo "usuario no existe. No se borro datos<br/>";echo "<p><a href='menu_usuario.html'>Haz clic aquí para intentar de nuevo</a></p>";};
			}else{echo"fallo conexio base de datos 1er intento. No se borro la cuenta";};
			//cerramos conexion
			off_table($conexion);	
		
			break;
		default:
			echo"Error al marcar boton radio<br/>";
			break;
	};
	
	
}


?>