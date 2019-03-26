<html>

<head>
<title>HelloW</title>
</head>
<body>

  <?php

echo "saving file...";

   $_id = $_GET["id"];
   $_time = $_GET["time"];
   $_data = $_GET["data"];

  echo "id equals $_id \n";
  echo "time equals $_time \n";
  echo "data equals $_data \n";
  echo getcwd();



   if ( $fl = fopen('logs.txt','a')) {
        fwrite($fl,"\"data\": { \"id\" : \"". $_id . "\", "
                              .\"time\" : \"". $_time . "\", "
                              ."\"data\" :\"" . $_data . "\" }\n" );
        fclose($fl);
      }

/*
       $myfile = fopen("C:\\Users\\romak\\Desktop\\CS\\Zilla downloads\\newfile.txt", "a") or die("Unable to open file!");
       $txt = "Minnie Mouse\n";
       fwrite($myfile, $txt);
       fclose($myfile);
*/
echo " complete";
    ?>

</body>
</html>
