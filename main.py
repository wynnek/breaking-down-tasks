import streamlit as st
from fuzzywuzzy import process
import datetime
from dateutil.relativedelta import relativedelta

packing_response = '''Here are some essential items to pack for a flight:

1. **Travel Documents**: Passport, driver's license, and boarding pass. Also consider bringing photocopies of these documents in case they get lost.

2. **Money**: Bring enough cash for your immediate needs, and don't forget your credit and debit cards.

3. **Electronics**: Phone, laptop, tablet, e-reader, chargers, and headphones. Consider bringing a portable power bank for charging on the go.

4. **Clothing**: Pack enough clothes for the duration of your trip, plus a few extra items in case of emergencies. Don't forget underwear, socks, and sleepwear.

5. **Toiletries**: Travel-sized shampoo, conditioner, body wash, toothpaste, and toothbrush. You might also want to pack a razor, deodorant, and any other personal hygiene items you use daily.

6. **Medication**: Any prescription medications you take, plus over-the-counter items like pain relievers, allergy medication, and band-aids.

7. **Snacks**: Pack some snacks for the flight, especially if it's a long one. Just make sure they comply with airport security regulations.

8. **Entertainment**: Books, magazines, or downloaded movies and music can help pass the time on a long flight.

9. **Comfort Items**: A travel pillow, blanket, and eye mask can make it easier to sleep on the plane.

10. **Miscellaneous**: Don't forget items like glasses or contact lenses, house keys, and any other essentials you'll need immediately upon landing.

Remember, every airline has its own rules about what you can bring on a flight, so be sure to check these before you start packing.'''

# Define a dictionary of keywords and responses
keywords = {
    'hello': 'Hello! How can I help you today?',
    'help': 'Sure, I can help. What do you need assistance with?',
    'pack': packing_response,
    'weather': 'Would you like me to check the weather for you?',
    'book': 'Do you need help booking something?',
    'flight': 'Do you need help booking a flight?',
    'hotel': 'Do you need help booking a hotel?',
    'lodging': 'Do you need help finding a place to stay?',
    'rental': 'Here are some popular car rental companies: 1. Hertz 2. Avis 3. Enterprise 4. Budget 5. Alamo',
    'transportation': 'Here are some popular transportation options: 1. Taxi 2. Uber 3. Lyft 4. Public transportation 5. Rental car',
    'gas': 'Here are some tips for saving money on gas: 1. Use a gas rewards credit card. 2. Shop around for the best prices. 3. Use a gas price app to find the cheapest stations. 4. Keep your car well-maintained for better fuel efficiency. 5. Consider carpooling or using public transportation to save on gas.',
    'food': 'Here are some tips for finding good food while traveling: 1. Ask locals for recommendations. 2. Use restaurant review apps like Yelp or TripAdvisor. 3. Look for places with a lot of customers, as this is a sign of good food. 4. Try the local cuisine for an authentic experience. 5. Be adventurous and try new things!',
    'attractions': 'Here are some popular attractions in the area: 1. Museums 2. Parks 3. Landmarks 4. Zoos 5. Aquariums',
    'currency': 'Here are some tips for exchanging currency: 1. Use ATMs for the best exchange rates. 2. Avoid currency exchange kiosks at airports and hotels, as they often have high fees. 3. Use credit cards for large purchases, as they often offer competitive exchange rates. 4. Be aware of any fees or commissions charged by your bank for foreign transactions. 5. Consider exchanging a small amount of currency before you leave for immediate expenses upon arrival.',
    'translate': 'Here are some popular translation apps: 1. Google Translate 2. Microsoft Translator 3. iTranslate 4. SayHi 5. TripLingo',
    'emergency': 'Here are some emergency numbers to keep in mind: 1. 911 (United States) 2. 999 (United Kingdom) 3. 112 (Europe) 4. 000 (Australia) 5. 119 (Brazil)',
    'disability': 'Here are some tips for traveling with a disability: 1. Contact the airline or hotel in advance to request any necessary accommodations. 2. Research the accessibility of your destination, including public transportation and attractions. 3. Pack any necessary medical supplies and medications in your carry-on luggage. 4. Consider using a travel agent who specializes in accessible travel. 5. Be prepared to advocate for yourself and your needs while traveling.',
    'pet': 'Here are some tips for traveling with a pet: 1. Check the airline\'s pet policy before booking your flight. 2. Make sure your pet is up-to-date on vaccinations and has a health certificate from the vet. 3. Pack a travel bag for your pet with food, water, bowls, toys, and any medications. 4. Consider using a pet carrier or crate for your pet\'s safety and comfort. 5. Be prepared for security screenings and customs checks with your pet.',
    'contact': 'Do you need help contacting someone?',
    'directions': 'Here are some popular navigation apps: 1. Google Maps 2. Waze 3. Apple Maps 4. MapQuest 5. Here WeGo',
    'wifi': 'Here are some tips for finding free wifi while traveling: 1. Look for cafes, restaurants, and hotels that offer free wifi. 2. Use wifi hotspots in public places like libraries, parks, and airports. 3. Consider purchasing a portable wifi device or a local SIM card for internet access. 4. Use wifi-finding apps like WifiMapper or Wifi Finder to locate free hotspots. 5. Be cautious when using public wifi networks, as they may not be secure.',
    'baggage': 'Here are some tips for dealing with lost or delayed baggage: 1. Report the issue to the airline immediately. 2. Fill out a baggage claim form and keep a copy for your records. 3. Provide the airline with a detailed description of your bag and its contents. 4. Keep all receipts for expenses related to the lost baggage. 5. Be patient and persistent in following up with the airline until the issue is resolved.',
    'security': 'Here are some tips for getting through airport security quickly: 1. Arrive early. 2. Wear slip-on shoes and avoid wearing jewelry or belts with metal. 3. Have your ID and boarding pass ready. 4. Follow the 3-1-1 rule for liquids. 5. Be prepared to remove your laptop from its case. 6. Be polite and cooperative with security personnel.',
    'boarding': 'Here are some tips for boarding a flight: 1. Listen for announcements. 2. Have your boarding pass and ID ready. 3. Follow the boarding groups. 4. Be prepared to stow your carry-on luggage quickly. 5. Find your seat and get settled as soon as possible. 6. Follow the instructions of the flight attendants.',
    'jet lag': 'Here are some popular methods for reducing jet lag during long flights: 1. Adjust your sleep schedule before you leave. 2. Stay hydrated and avoid alcohol and caffeine. 3. Get some exercise and fresh air upon arrival. 4. Consider taking melatonin or other sleep aids. 5. Take short naps to help you adjust to the new time zone.',
    'human': 'Would you like to talk to a human? Too bad! I\'m here to help!',
    'goodbye': 'Goodbye! Have a great day!',
}


def get_response(message):
    # Use fuzzy matching to find the closest keyword
    keyword, score = process.extractOne(message.lower(), keywords.keys())

    # Only use the match if the score is above a certain threshold (e.g., 80)
    if score > 80:
        return keywords[keyword]
    else:
        return 'Sorry, I did not understand that. Could you please rephrase?'

# Create the Streamlit app
st.title('Winging It Wisely')
st.write('Hey! I\'m WIW. Think of me as your flight planner. If you have a flight or a long roadtrip to plan, please allow me break down what you need to do to prepare for your trip!')

# Ask for demographic information
st.write('First, could you please provide some information about yourself?')
name = st.text_input('Name:')
age = st.number_input('Age:', min_value=0, max_value=120)
country = st.text_input('Passport Country:')
num_passengers = st.number_input('Number of Passengers:', min_value=1, max_value=100, value=1)
language = st.selectbox('Language:', options=['English'])
st.write('Sorry, we only support English right now. Let\'s get started!')
trip_type = st.selectbox('Type of Trip:', options=['Flight (International)', 'Flight (Domestic)', 'Roadtrip'])
st.write('Plans change. We know. So currently, we only deal with one-way trips. Please enter the origin and destination cities, as well as the departure date below:')

next_month = datetime.date.today() + relativedelta(months=+1)

origin = st.text_input('Origin City:')
departure_date = st.date_input('Departure Date:', value=next_month)

destination = st.text_input('Destination City:')
arrival_date = st.date_input('Arrival Date:', value=next_month + datetime.timedelta(weeks=1))

# Check that the origin city and the destination city are not the same
if origin and destination:  # Only check if both fields have been filled out
    if origin == destination:
        st.error('The origin city and the destination city cannot be the same. Please enter different cities.')

# Check that the departure date and return date are not the same
if departure_date and arrival_date:  # Only check if both fields have been filled out
    if departure_date == arrival_date:
        st.error('The departure date and arrival date cannot be the same. Please enter different dates.')

# Ask for the task to simplify
user_message = st.text_input('Enter a task you\'d like to simplify (e.g. packing, booking the flight/hotel, lodging, transportation, gas):')
if user_message:
    response = get_response(user_message)
    st.write(f'{name}, {response}')

