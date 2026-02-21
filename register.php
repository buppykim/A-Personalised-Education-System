<?php
include 'connect.php';
 if(isset ($_POST['signup'])){
    $firstName=$_POST ['fname'];
    $lastName=$_POST ['lname'];
    $email=$_POST ['email'];
    $password=$_POST ['password'];
    $confirmPassword=$_POST ['cpassword'];
    $password=md5($password);

    $checkEmail = "SELECT * FROM users WHERE email = '$email'";
    $result = mysqli_query($conn, $checkEmail);
    if($result->num_rows > 0){
        echo "Email already exists";
    }else{
        $sql = "INSERT INTO users (firstName, lastName, email, password) VALUES ('$firstName', '$lastName', '$email', '$password')";
        if($conn->query($sql) === TRUE){
            echo "Registration successful";
            header('location:index.html');
        }else{
            echo "Registration failed";
        }
      if(isset($_POST['login'])){
        $email=$_POST ['email'];
$password=$_POST ['password'];
$password=md5($password);
$sql = "SELECT * FROM users WHERE email = '$email' AND password = '$password'";
$result = $conn_query($sql);
if($result->num_rows > 0){
    sessin_start();
    $row=$result->fetch_assoc();
    $_SESSION['email']=$row['email'];
    header('location:index.html');
    exit();
}
    else{
        echo "Invalid email or password";
    }
}
    }
}
?>