from __future__ import print_function
import time
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException
from pprint import pprint

import json

# Configure API key authorization: Apikey
configuration = cloudmersive_barcode_api_client.Configuration()
configuration.api_key['Apikey'] = 'ed643fd3-d280-4c74-8c98-6068a494b510'



# create an instance of the API class
api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
image_file = 'barcode_img/test4.jpg' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Scan an image for a barcode and turn the result.  Supported barcode types include AZTEC, CODABAR, CODE_39, CODE_93, CODE_128, DATA_MATRIX, EAN_8, EAN_13, ITF, MAXICODE, PDF_417, QR_CODE, RSS_14, RSS_EXPANDED, UPC_A, UPC_E, All_1D, UPC_EAN_EXTENSION, MSI, PLESSEY, IMB
    api_response = api_instance.barcode_scan_image(image_file)
    pprint(api_response)
    barcodeNum = api_response['raw_text']

except ApiException as e:
    print("Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" % e)