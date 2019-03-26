<html><body>
<?php
   $user = "muntean";
   require '/var/composer/vendor/autoload.php';
   $manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
   $collection = new MongoDB\Collection($manager, $user, 'testData');
   $ts = new MongoDB\BSON\Timestamp(0,0);
   # Get JSON as a string
   if ($_SERVER['REQUEST_METHOD'] === 'POST') {
      var_dump($_POST);
      $json_str = $_POST['json'];
   }
   else if ($_SERVER['REQUEST_METHOD'] === 'GET') {
      $json_str = $_GET['json'];
   }
   else {
      $json_str = file_get_contents('php://input');
   }
   # Decode
   $json_obj = json_decode($json_str, true);
   print(json_last_error());
   print("Request: ");
   print_r($json_str);
   print("<br>Array: ");
   var_dump($json_obj);
   print("<br>");
   $myfile = file_put_contents('logs.txt', $json_str.PHP_EOL , FILE_APPEND | LOCK_EX);
   try {
      $collection->insertOne($json_obj);
   } catch (\Exception $e) {
      print("Insert failed.");
      print_r($e);
      exit();
   }
   $filter = [];
   $options = [];
   $query = new MongoDB\Driver\Query($filter, $options);
   $cursor = $manager->executeQuery("$user.testData", $query);
   print("The contents of the collection $user.testData are:");
   print_r($cursor->toArray());
?>
