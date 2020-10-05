"""
This automated test will do the following
1. Call the Get API method.
2. Load the response in JSON format
3. Filter the asset names that have the desired aspect ratio and resolution which is mentioned on the conf file.
4. Create a CSV file and load the fetched asset names in it.
"""

import csv, os, requests
import conf

def create_csv(filename, asset_id):
    "To write the fetched asset id's in csv file"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        for asset in asset_id:
            columns = [c.strip() for c in asset.strip(', ').split(',')]
            csvwriter.writerow(columns)

if __name__ == "__main__":
    response = requests.get(conf.get_media_info_api, params=conf.payload)
    data = response.json()
    asset_id = []
    if data!= "":
        for d in data["media"]:
            filename = d["filename"]
            try:
                aspect_ratio = d["video"]["aspect_ratio"]
                resolution = d["resolution"]
                if aspect_ratio==conf.ratio and resolution==conf.resolution:
                    asset_id.append(os.path.splitext(filename.split('/')[-1])[0])
            except:
                print(f"Either Aspect ratio or resolution for {filename} was not found. Please verify this asset in the Media Library")
        create_csv("reprocess.csv",asset_id)