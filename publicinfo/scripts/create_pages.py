from person.models import Person, Page
import requests

states = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


def get_pages():
    objs = Page.objects.all()
    print(len(objs))


def get_persons():
    objs = Person.objects.all()
    for obj in objs:
        print(obj.first_name)

def create_pages():
    variations = ['full name', 'firs name last name', 'last name first name', 'facebook nickname']
    person_objs = Person.objects.all()
    for person in person_objs:
        i = 0
        for v in variations:
            if i == 0:
                if person.middle_name:
                    slug = '{0}-{1}-{2}'.format(person.first_name, person.middle_name, person.last_name)
                else:
                    slug = '{0}-{1}'.format(person.first_name, person.last_name)
            elif i == 1:
                slug = '{0}-{1}'.format(person.first_name, person.last_name)
            elif i == 2:
                slug = '{0}-{1}'.format(person.last_name, person.first_name)
            elif i == 3:
                slug = '{0}'.format(person.nick_name)
            else:
                slug = '{0}-{1}'.format(person.first_name, person.last_name)
            i = i + 1
            for state in states.keys():
                get_cities_api_link = 'http://api.sba.gov/geodata/city_data_for_state_of/{0}.json'.format(state)
                r = requests.get(get_cities_api_link)
                if r.status_code == 200:
                    for county in r.json():
                        page_obj = Page(
                            person = person,
                            slug = slug,
                            city = county['county_name'],
                            state = state,
                            country = 'US',
                            zipcode = person.zipcode,
                            title = 'ResidentsInfo.com | {0} - {1} - {2}'.format(
                                slug,
                                states[state],
                                county['county_name']
                            ),
                            description = 'Resident Details: {0} , State: {1}, City: {2}, Facebook: {3}, Linkedin: {4}, Phone Number: {5}'.format(
                                slug,
                                states[state],
                                county['county_name'],
                                person.facebook_link,
                                person.linkedin_link,
                                person.phone_number
                            ),
                            primary_latitude = county['primary_latitude'],
                            primary_longitude = county['primary_longitude']
                        )
                        page_obj.save()

create_pages()
get_pages()
