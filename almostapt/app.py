import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from exceptions.mongodb_error import BasePyMongoException
import csv
from pathlib import Path

load_dotenv()

app = Flask(__name__)
mongodb_username = os.getenv('MONGODB_USERNAME')
mongodb_password = os.getenv('MONGODB_PASSWORD')
mongo_client = MongoClient(
    f"mongodb+srv://{mongodb_username}:{mongodb_password}@your.db_info.mongodb.net/?retryWrites=true&w=majority",
     authSource="admin", serverSelectionTimeoutMS=5000, server_api=ServerApi('1')
)
almostapt_db = mongo_client['almostaptdb']
almostapt_collection = almostapt_db['almostaptcoll']
almostapt_collection.create_index([("group_name", pymongo.TEXT)])


def search_mongodb(group_name):
    group = almostapt_collection.find({"$text": {"$search": group_name}})
    return group

def load_group_from_csv():
    groups = []
    root_path = Path(app.root_path) / 'data'
    csv_file = root_path / 'almost_apt_groups.csv'
    
    with open(csv_file, newline='', encoding='utf-8-sig')as csv_file:
        reader = csv.DictReader(csv_file)
        
        for rows in reader:
            groups.append(rows)
    
    return groups


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        count_documents = almostapt_collection.count_documents({})
    except BasePyMongoException:
        flash('There was an issue connecting to the database. Please try again', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        group_name = request.form['search']
        return redirect(url_for('group_info', group_name=group_name))
    return render_template("base.html", count_documents=count_documents)


@app.route("/group_info/<group_name>")
def group_info(group_name):
    
    group = search_mongodb(group_name)
    threat_group_results = list(group)
    
    country = ''.join(
        result['operating_region'] + ', ' for result in threat_group_results
    )
    country = country.rstrip(', ')
    if group:
       
        return render_template('searchresults.html', groups=threat_group_results, country=country)
   
    return render_template('not_found.html', group_name=group_name)
    

@app.route('/groups')
def group_list():
    groups = load_group_from_csv()

    for group_card in groups:
        if group_card['country'] == 'UNK':

            group_card['css_flag'] = 'fas fa-question-circle'
        else:
            group_card['css_flag'] = f"flag-icon flag-icon-{group_card['css_flag']}"
    return render_template('all_groups.html', groups=groups)


@app.errorhandler(404)
def not_found_page(err):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(err):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
