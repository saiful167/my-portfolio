<?php
$ip = $_SERVER['REMOTE_ADDR'];
$agent = $_POST['browser'] ?? 'unknown';
$time = date("Y-m-d H:i:s");

// Get IP Location using ipinfo.io (basic)
$location = @file_get_contents("http://ipinfo.io/{$ip}/json");
$log = "$time | IP: $ip | Agent: $agent | Location: $location\n";

// Save to file
file_put_contents("attackers.log", $log, FILE_APPEND);
?>
