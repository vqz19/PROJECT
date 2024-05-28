import os
from flask import Blueprint, request, redirect
from flask import render_template, url_for
from flask import send_file


import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    level=logging.DEBUG,
                    force=True)


logger = logging.getLogger(__name__)

MANAGER_RESOURCE = Blueprint("manager_resource", __name__)


@MANAGER_RESOURCE.route("/secret-manager",
                        methods=["GET"])
def secrets_home():
    return render_template("pages/secret_manager.html")


@MANAGER_RESOURCE.route("/secret-manager2",
                        methods=["GET"])
def secrets_home2():
    return render_template("layout/index.html")


@MANAGER_RESOURCE.route("/secret-manager",
                        methods=["POST"])
def import_secrets():
    
    logger.info(request.files)
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '' or not file.filename.endswith(".csv"):
            return redirect(url_for("manager_resource.secrets_home2"))
        file.save(os.path.join(os.getcwd(), "secret_manager\src\service", "file.csv"))
    return redirect(url_for("manager_resource.secrets_home"))


@MANAGER_RESOURCE.route("/secret-manager/export_docs",
                        methods=["POST"])
def export_secrets():
    return send_file(os.path.join(os.getcwd(), "secret_manager\src\service", "file.csv"), download_name="prueba.csv" ) 


@MANAGER_RESOURCE.route("/secret-manager/import_docs",
                        methods=["GET"])

def page_import_secrets():
    return render_template("pages/import_files.html")


@MANAGER_RESOURCE.route("/secret-manager/export_docs",
                        methods=["GET"])

def page_export_secrets():
    return render_template("pages/export_files.html")


@MANAGER_RESOURCE.route("/add-items",
                        methods=["GET"])

def page_add_items():
    return render_template("pages/add_item.html")

@MANAGER_RESOURCE.route("/add-items",
                        methods=["POST"])

def page_create_item():
    return render_template("pages/add_item.html")