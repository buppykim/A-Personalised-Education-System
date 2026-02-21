<?php
$host="localhost";
$user="root";
$password="";
$db="login";
$conn=new mysqli_connect($host,$user,$password,$db);
if($conn->connect_error){
    echo "connection failed DB".$conn->connect_error;
}
?> 