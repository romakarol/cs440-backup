<html>
  <head>
   <title>Demonstrateur SigFox</title>
  </head>
  <body>
  <?php
     $_id = $_GET["id"];
     $_time = $_GET["time"];
     #$_signal = $_GET["signal"];
     #$_station = $_GET["station"];
     #$_lat = $_GET["lat"];
     #$_lng = $_GET["lng"];
     $_data = $_GET["data"];

     echo hex2bin ($_data); #echoes nothing
     echo hex2bin ("$_data"); #echoes nothing
     echo hex2bin("39715100"); #echoes 9qQ
     echo ("shouldBE");

     if ( $fl = fopen('logs.txt','a')) {
       fwrite($fl,"\"msg\": { \"id\" : \"". $_time . "\", "
                            ."\"data\" :\"" . $_data . "\" }\n" );
       fclose($fl);
     }
  ?>
  </body>
</html>
