import os
from minio import Minio

if __name__ == "__main__":
    data = {"url": "devops.civil3.xyz:30090", "accessKey": "eCUkmwLJeiO0ftO0",
            "secretKey": "7D51hWycGiQb6oakgsMLzkhkkbcIIOtb",
            "api": "s3v4", "path": "auto"}
    minio_client = Minio(endpoint=data.get("url"), access_key=data.get("accessKey"), secret_key=data.get("secretKey"),
                         secure=False)
    with open("build/app/outputs/flutter-apk/app-release.apk", mode="rb") as fp:
        file_stat = os.stat(fp.name)
        minio_client.put_object("apk", "android-release.apk", data=fp, length=file_stat.st_size)
