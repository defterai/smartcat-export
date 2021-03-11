#!/usr/bin/python

import sys
import time
import configparser
from smartcat import *

def export_multilang_csv(document_resource, document_id, output_file_name):
    print(f'Export document: {output_file_name}')
    with document_resource.request_export(document_ids=document_id, target_type='multilang_Csv') as export_result:
        if export_result.status_code != 200:
            print('Error: Failed request status code - ', export_result.status_code)
            return 1
        print('Export started')
        export_json = json.loads(export_result.text)
        export_task_id = export_json['id']
        wait_download_ready = False
        try:
            while True:
                with document_resource.download_export_result(export_task_id) as download_result:
                    if download_result.status_code == 200:
                        if wait_download_ready:
                            print('')
                        wait_download_ready = False
                        print('Download started')
                        with open(output_file_name, 'wb') as out_file:
                            for chunk in download_result.iter_content(chunk_size=8192):
                                out_file.write(chunk)
                        print('Download completed')
                        break
                    elif download_result.status_code == 204:
                        if wait_download_ready:
                            print('.', end='')
                        else:
                            print('Wait download ready', end='')
                            wait_download_ready = True
                        time.sleep(1)
                    else:
                        if wait_download_ready:
                            print('')
                        print('Error: export status code - ', download_result.status_code)
                        return 1
        except:
            if wait_download_ready:
                print('')
            raise
        print('Export completed')
        return 0

def main(args):
    if len(args) != 6:
        print('Error: Wrong script parameters')
        return 1
    result = 1
    try:
        accountId = args[1]
        authKey = args[2]
        documentId = args[3]
        languageId = args[4]
        outputFilename = args[5]
        api = SmartCAT(accountId, authKey, SmartCAT.SERVER_EUROPE)
        result = export_multilang_csv(api.document, documentId + '_' + languageId, outputFilename)
    except Exception as err:
        print('Error: Failed export: {0}'.format(err))
    except KeyboardInterrupt as err:
        print('Interrupted')
    if result == 0:
        print('Done')
    return result

if __name__ == "__main__":
    sys.exit(main(sys.argv))
