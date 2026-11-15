import sqlite3

# Define the columns for our database table
COLUMNS = [
    "name", "icon", "category", "status", "status_label", "years", "location",
    "coordinates", "launch", "discovery", "final", "science", "fun_fact"
]

# The data for each artifact
ROWS = [
    ("Apollo 11 Descent Stage", "🌕", "moon", "silent", "Silent since 1969", "Landed 1969",
     "The Moon (Sea of Tranquility)", "0.674° N, 23.473° E",
     "On 20 July 1969, the Lunar Module “Eagle” touched down with Neil Armstrong and Buzz Aldrin aboard.",
     "After their moonwalk, the astronauts blasted off in the top half of Eagle, using the descent stage as a launch pad. They carried home about 21 kg of Moon rock.",
     "The descent stage never moved again. It still sits in the Sea of Tranquility, and orbiting cameras have photographed it from above.",
     "The crew also left a mirror-like laser reflector nearby. Scientists still bounce lasers off it to measure the Earth–Moon distance.",
     "A plaque on its leg reads “We came in peace for all mankind.”"),
    
    ("Apollo 15 Lunar Rover", "🚙", "moon", "silent", "Parked since 1971", "Landed 1971",
     "The Moon (Hadley–Apennine)", "26.13° N, 3.63° E (landing site)",
     "Folded up inside Apollo 15’s lander, the first Lunar Roving Vehicle was unpacked in July 1971.",
     "Astronauts David Scott and James Irwin drove it about 28 km, reaching places they could never have walked to, and gathered around 77 kg of Moon rocks.",
     "Scott parked it where its TV camera could watch the liftoff. It is still parked there today.",
     "The rocks it helped collect revealed how the Moon’s crust formed, including the famous “Genesis Rock”.",
     "On this mission, Scott dropped a hammer and a feather together on the Moon, and they landed at the same time."),
    
    ("Opportunity Rover", "🤖", "mars", "silent", "Silent since 2018", "2004–2018",
     "Mars (Meridiani Planum)", "1.95° S, 354.47° E (landing site)",
     "Opportunity landed on 25 January 2004 and was built for a 90-day mission.",
     "It kept going for about 14 years and drove 45 km. It found tiny iron-rich spheres nicknamed “blueberries” and rocks that formed in water.",
     "A huge dust storm blocked its sunlight in 2018. Engineers sent more than a thousand recovery commands, but it never replied. NASA ended the mission in February 2019.",
     "Opportunity showed that ancient Mars had watery places that could have supported life.",
     "Its final data were poetically translated as “My battery is low and it’s getting dark.”"),
    
    ("Viking 1 Lander", "📡", "mars", "silent", "Silent since 1982", "1976–1982",
     "Mars (Chryse Planitia)", "22.48° N, 47.97° W",
     "On 20 July 1976, Viking 1 became the first NASA spacecraft to land and work on Mars.",
     "It sent back the first close-up pictures from the Martian surface and ran experiments to look for signs of life in the soil.",
     "It worked for more than six years. In 1982 a mistaken update left its antenna pointing away from Earth, and it was never heard from again.",
     "Its weather station recorded Mars’s seasons, and its soil tests gave results that scientists still debate.",
     "It landed exactly seven years after Apollo 11’s Moon landing."),
    
    ("Ingenuity Helicopter", "🚁", "mars", "silent", "Retired in 2024", "2021–2024",
     "Mars (Jezero Crater)", "≈ 18.4° N, 77.5° E",
     "This tiny helicopter rode to Mars on the Perseverance rover and landed on 18 February 2021.",
     "On 19 April 2021 it made the first powered flight on another planet. It was meant to fly 5 times and flew 72.",
     "In January 2024 a rough landing damaged its rotor blades. NASA ended its mission, and it stays on Mars.",
     "It proved that flying on Mars is possible, even though the air is about 100 times thinner than on Earth.",
     "It carried a tiny piece of fabric from the Wright brothers’ 1903 airplane."),
    
    ("Voyager 1", "🛰️", "deep", "active", "Still sending data", "1977–today",
     "Interstellar space", "Over 25 billion km from Earth",
     "Launched on 5 September 1977 to visit Jupiter and Saturn.",
     "It found erupting volcanoes on Jupiter’s moon Io and, in 1990, took the “Pale Blue Dot” photo of Earth from billions of kilometres away.",
     "In 2012 it became the first human-made object to enter interstellar space. It is still sending data home.",
     "It showed scientists what the edge of the Sun’s bubble of particles is like, and it still measures the space between the stars.",
     "It carries a Golden Record with sounds and pictures from Earth. A radio signal now takes about a day to reach it."),
    
    ("Voyager 2", "🛰️", "deep", "active", "Still sending data", "1977–today",
     "Interstellar space", "Over 20 billion km from Earth",
     "Launched on 20 August 1977, 16 days before Voyager 1, on a grand tour of the giant planets.",
     "It is the only spacecraft ever to visit Uranus (1986) and Neptune (1989), where it found new moons and rings.",
     "It entered interstellar space in 2018 and is still sending data.",
     "Its flybys revealed Uranus’s tilted magnetic field, Neptune’s fast winds and icy geysers on Triton.",
     "Its twin launched later but moved faster, so Voyager 1 is farther away."),
    
    ("Pioneer 10", "🌠", "deep", "silent", "Silent since 2003", "1972–2003",
     "Deep space", "Heading toward the star Aldebaran",
     "Launched on 2 March 1972 to find out whether a spacecraft could cross the asteroid belt.",
     "It survived the belt and became the first spacecraft to fly past Jupiter in December 1973, measuring the planet’s dangerous radiation.",
     "Its last signal reached Earth on 23 January 2003. It is still drifting through space, but too far away to hear.",
     "It paved the way for later missions by showing that the asteroid belt and Jupiter’s radiation could be survived.",
     "It carries a gold plaque showing a man, a woman and Earth’s location, and will pass near Aldebaran in about 2 million years.")
]

def initialize_database():
    # Connect to the database file
    conn = sqlite3.connect("space_museum.db")
    cur = conn.cursor()
    
    # Delete the table if it already exists to start fresh
    cur.execute("DROP TABLE IF EXISTS artifacts")
    
    # Create the table with all 13 columns
    cur.execute('''
        CREATE TABLE artifacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            icon TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL,
            status_label TEXT NOT NULL,
            years TEXT NOT NULL,
            location TEXT NOT NULL,
            coordinates TEXT NOT NULL,
            launch TEXT NOT NULL,
            discovery TEXT NOT NULL,
            final TEXT NOT NULL,
            science TEXT NOT NULL,
            fun_fact TEXT NOT NULL
        )
    ''')
    
    # Insert all rows into the database using parameterized queries (?)
    cur.executemany('''
        INSERT INTO artifacts (
            name, icon, category, status, status_label, years, location, 
            coordinates, launch, discovery, final, science, fun_fact
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', ROWS)
    
    # Save and close
    conn.commit()
    conn.close()
    print("Database 'space_museum.db' initialized with", len(ROWS), "exhibits!")

if __name__ == "__main__":
    initialize_database()
