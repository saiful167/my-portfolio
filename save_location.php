<?php
if (isset($_POST['latitude']) && isset($_POST['longitude'])) {
    $lat = $_POST['latitude'];
    $lon = $_POST['longitude'];
    $ip = $_SERVER['REMOTE_ADDR'];
    $time = date("Y-m-d H:i:s");

    $log = "$time | IP: $ip | Latitude: $lat | Longitude: $lon\n";
    file_put_contents("locations.txt", $log, FILE_APPEND);
}
?>
