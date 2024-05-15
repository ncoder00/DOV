from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify
from util.validation import is_valid_domain, is_valid_ip
from util.whois_lookup import get_whois_lookup
from util.dns_lookup import get_dns_lookup
from util.ssl_cert import ssl_cert_details
from util.http_header import get_http_headers
from util.geolocation import get_geolocation

def format_datetime(value, format="%Y-%m-%d %H:%M:%S"):
    if isinstance(value, list):
        return [format_datetime(v, format) for v in value]
    elif isinstance(value, datetime):
        return value.strftime(format)
    return value

def setup_routes(app):
    app.jinja_env.filters['format_datetime'] = format_datetime

    @app.route('/', methods=['GET', 'POST'])
    def home():
        error_message = None
        if request.method == 'POST':
            user_input = request.form.get('user_input', '').strip()
            valid_domain, sanitized_domain = is_valid_domain(user_input)
            valid_ip, sanitized_ip = is_valid_ip(user_input)
            if valid_domain:
                return redirect(url_for('results', input=sanitized_domain))
            elif valid_ip:
                return redirect(url_for('results', input=sanitized_ip))
            else:
                error_message = "Invalid input. Please enter a valid IP address or domain name without extra spaces or special characters."
                return render_template('home.html', error=error_message)
        return render_template('home.html')

    @app.route('/results/<input>')
    def results(input):
        whois_results = get_whois_lookup(input)
        geolocation_results = get_geolocation(input)
        data = {'whois_results': whois_results, 'geolocation_results': geolocation_results}
        
        if is_valid_domain(input)[0]:
            dns_results = get_dns_lookup(input)
            ssl_results = ssl_cert_details(input)
            http_header_results = get_http_headers(input)
            data.update({
                'dns_results': dns_results,
                'ssl_results': ssl_results,
                'http_header_results': http_header_results,
                'geolocation_results': geolocation_results,
            })
        
        return jsonify(data)
