<?php

$Regex_Pattern = '/^\d\d(?|(-)|(---)|(.)|(:))(\d\d\1){2}\d\d$/';


$handle = fopen ("php://stdin","r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print ("true");
} else {
    print ("false");
}

fclose($handle);
?>
