import time
import datetime
import pprint

class Report:
    def __init__(self):
        pass

    def str_date_time_to_timestamp(self, dt):
        date_time_obj = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
        tuple = date_time_obj.timetuple()
        timestamp = time.mktime(tuple)
        return int(timestamp)

    def filter_reports(self, reports, filter_by):
        compare_date = self.str_date_time_to_timestamp("2020-01-01 00:00:00")
        if filter_by == "date":
            data = []
            for item in reports:
                try:
                    item_timestamp = self.str_date_time_to_timestamp(
                        item.get("createdDate")
                    )
                    if item_timestamp >= compare_date:
                        data.append({
                            "ID": item.get("ID"),
                            "Device_ID": item.get("Device_ID"),
                            "Location": item.get("Location"),
                            "createdDate": item.get("createdDate"),
                        })
                    else:
                        continue
                except:
                    continue
            return data
        elif filter_by == "latest_report":
            maximum_date = None
            data = None
            for item in reports:
                try:
                    item_timestamp = self.str_date_time_to_timestamp(
                        item.get("createdDate")
                    )
                    if maximum_date == None:
                        maximum_date = item_timestamp
                        data =  item
                    elif item_timestamp > maximum_date:
                            maximum_date = item_timestamp
                            data = item
                except:
                    continue
            return data
        else:
            return None

    def filter_report_by_date(self, reports):
        return self.filter_reports(reports, "date")

    def get_latest_report(self, reports):
       return self.filter_reports(reports, "latest_report")

if _name_ == '_main_':
    ## create report Object
    report = Report()
    ## filter reports >= 2020-01-01 from list of reports
    reports = [
        {
            "ID": 1,
            "Device_ID": 101,
            "Location": 'Helsinki',
            "createdDate": '2019-01-01 12:00:04',
        },
        {
            "ID": 3,
            "Device_ID": 103,
            "Location": 'Pori',
            "createdDate": '2020-01-01 12:00:04',
        },
        {
            "ID": 2,
            "Device_ID": 102,
            "Location": 'Oulu',
            "createdDate": '2019-04-01 15:09:00',
        },
        {
            "ID": 4,
            "Device_ID": 104,
            "Location": 'Tampere',
            "createdDate": '2020-12-01 10:08:00',
        },
        {
            "ID": 5,
            "Device_ID": 105,
            "Location": 'Turku',
            "createdDate": '2020-11-11 9:00:00',
        },
        {
            "ID": 6,
            "Device_ID": 106,
            "Location": 'Paris',
            "createdDate": '2020-01-23 06:11:00',
        }]

    report_filtered_by_date = report.filter_report_by_date(reports)
    # print the reports >= 2020-01-01
    print("### reports >= 2020-01-01 \n")
    pprint.pprint(report_filtered_by_date)

    print("\n")

    ## Get the maximum report from list of reports
    maximum_report = report.get_latest_report(reports)
    print("### latest/maximum report \n")
    # print the latest/maximum report
    pprint.pprint(maximum_report)