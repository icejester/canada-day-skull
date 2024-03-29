# CANADA DAY SKULL - MADE WITH PRIDE!
<img src="images/pskul-fin-resin.gif" width="600"/>

# Origin story
So if you've gotten around to this release, you likely know that this project was started because of my buddy and his Canada Day party. If you're not familliar with the origin story, I highly suggest checking out [the original.](https://github.com/icejester/canada-day-skull/tree/cds-v1.0.0)

# Time marches on
I've made a few of these skulls since the first one. I wanted one of my own so on Canada Day 2022, I walked out of the Canada Day party with a skull of my very own. As fate would have it, it was one of the ["Made With Pride"](https://www.crystalheadvodka.com/news/made-with-pride) skull bottles, which I thought was pretty cool.   

# Construction

I wanted to focus more on documenting the construction process this time around. I missed several aspects the first time, so I'd like to focus on them here.

### Scaffolding 

<img src="images/scaffold-1.jpg" width="250"/> <img src="images/scaffold-2.jpg" width="250"/> <img src="images/scaffold-3.jpg" width="250"/>

One of the things I wanted to improve on with the first iteration was how the loose LEDs in the jar would "clump up" and the skull would have light and dark spots. I wanted the lights to be spread out over the entire volume. I settled on a piece of ridgid copper shielded wire (12 GA) formed into a spiral. The first iteration I used double sided tape to secure the LEDs to the scaffolding. I've used several variations of electrical tape and even hockey tape.

### Soldering:

I really enjoy soldering and as such, bought myself a nice work station with a lighted magnifier. I can not tell you how much "proper tooling" has improved my soldering ability. If you love these kind of hibbies, spend the money. It'll be worth it. Yes there's a ton of unrelated crap on my bench. No I didn't put it there to make me look handy. Yes, I'm just that disorganized.

<img src="images/solder-1.jpg" width="600"/> <img src="images/solder-2.jpg" width="300"/> <img src="images/solder-3.jpg" width="300"/>

### The circuit

I used an [adafruit trinket](https://www.adafruit.com/product/3500), some [neopixels](https://www.adafruit.com/product/3851) and silicone shielded wire. The schematic is pretty simple. The board and the LED strip are powered directly from the battery, A signal wire (blue) from pin 3 to the signal on the LED strip, and a signal wire from the touch capacitive port (1~) on the board:

<img src="images/schematic.jpg" width="400"/>

### The hole... no, really

Of all the steps involved in this project, drilling the hole has the most risk and anxiety. I was quite happy with the hole drilling this time as I no longer had my "good vice" so I had to drill the skull "free hand."

<img src="images/pdrill-hole.jpg" width="600"/>

### The Resin 
In years past I have always done "glass" resin to accent the internals. I even went so far as to do one in multiple pours with differnet colors. This year, my daughter suggested I "pearlize" the resin with mica powder. I took some pictures between pours to capture how well the pearlization diffuses the light

<img src="images/pskul-1.gif" width="250"/> <img src="images/rwskull-1.jpg" width="250"/> <img src="images/pskul-2.gif" width="250"/> 

# The software
I didn't do a whole lot different this time with exception to what I'm calling the blinkFade method. I wanted something that would look like randomly starting lights that faded away over time. I think this was a pretty succinct way to get that done.

```
def blinkFade():
    # print("blinking")
    currentLitPixels = 0
    # count total lit pixels
    for p in range(NUMPIXELS):
        aPixel = neopixels[p]
        if aPixel[0] > 10:
            rCur = aPixel[0]
            gCur = aPixel[1]
            bCur = aPixel[2]
            
            neopixels[p] = ((rCur - 10, gCur - 10, bCur - 10))
            currentLitPixels += 1
    
    # if the number of lit pixels is less than max lit pixels
    if currentLitPixels < 15:
        neopixels[random.randint(0,29)] = (250, 250, 250)
```