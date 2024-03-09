import boto3
from flask import current_app
from werkzeug.utils import secure_filename

s3 = boto3.client("s3")

def upload_file_to_s3(file, resource_path):
    filename = secure_filename(file.filename)
    object_name = f"{resource_path}/{filename}"
    s3.upload_fileobj(
        file,
        current_app.config["AWS_BUCKET_NAME"],
        object_name,
        ExtraArgs={"ContentType": file.content_type},
    )
    return object_name

def generate_s3_signed_url(object_name):
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": current_app.config["AWS_BUCKET_NAME"], "Key": object_name},
        ExpiresIn=3600,
    )
 