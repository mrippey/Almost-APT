from flask import Blueprint, render_template, request, flash
import pymongo


mongodb_url = ''

main = Blueprint(
    "main",
    __name__,
    static_folder="",
    template_folder="templates"
)

# basic route
@main.route('/')
@main.route('/home')
def home():
    
    if "search" in request.args:
        # initialize and connect db
        conn_mongo_cli = pymongo.MongoClient(mongodb_url,authSource="admin")

        db = conn_mongo_cli["tagroupdb"]

        db_collection = db.tagroups

        # create index
        db_collection.create_index(
        [("vendor_des", pymongo.TEXT), ("name", pymongo.TEXT)])

        threat_group = db_collection.find(
            {"$text": {"$search": request.args.get("search")}})

        for entries in threat_group:
            flash(entries, "success")

        conn_mongo_cli.close()

    return render_template("search_home.html")
    

@main.route("/threat_group")
def threat_group():

    if "search" in request.args:
        # initialize and connect db
        conn_mongo_cli = pymongo.MongoClient(mongodb_url, authSource="admin")

        db = conn_mongo_cli["tagroupdb"]

        db_collection = db.tagroups
    
        db_collection.create_index([("vendor_des", pymongo.TEXT), ("name", pymongo.TEXT)])

        threat_group = db_collection.find(
            {"$text": {"$search": request.args.get("search")}})

        threat_group_results = [entries for entries in threat_group]

        total_results = len(threat_group_results)

        conn_mongo_cli.close()

 
    return render_template("threat_group.html", 
        data=threat_group_results, 
        length=total_results)
