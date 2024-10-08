# CANADA DAY SKULL - TERMINATOR EDITION!!
<img src="images/silverSkull.jpeg" width="600"/>

# Origin story
So if you've gotten around to this release, you likely know that this project was started because of my buddy and his Canada Day party. If you're not familliar with the origin story, I highly suggest checking out [the original.](https://github.com/icejester/canada-day-skull/tree/cds-v1.0.0)

After taking in the origin story, I'd encourage you to check out "V2" which is also known as [the Pride Skull.](https://github.com/icejester/canada-day-skull/tree/cds-v2.0.0)

# Into each life, a little rain must fall

<img src="images/shatteredSkull.jpeg" width="600"/>

Unfortunately... shortly after my own summer party, the Pride Skull mysteriously shattered. There was no rhyme or reason to it. I walked into my office one day, and the front of the skull had popped off and there were several other cracks in the skull bottle, but the resin stayed in tact. All of the electrical components were in tact and functional. This was totally repairable with a little time, effort, and energy. 

# Construction

I honestly dragged my feet a bit this year and the fact that I also wanted to repair the pride skull left me little to no time to really do anything new for construction. I set myself to the task of repairing the pride skull. 

### Repair

<img src="images/prideBreak-1.jpeg" width="250"/> <img src="images/prideBreak-3.gif" width="250"/> <img src="images/prideBreak-2.jpeg" width="250"/>

I used a dremel to sand down the edges of the broken glass then used E-6000 to glue them back in place. I had originally planned to shave the glass pieces down enough to fill the resulting gaps with tile grout, but I couldn't seem to take enough off the pieces. Without at least 1/6th of an inch, I couldn't use the grout, I was stuck. I got the idea of trying to pour resin into the cracks hoping it would work similar to grout. The resin was WAY too thin immediately after stirring. After the fitst pour, I noticed the resin was just running off the sidesof the skull. I then decided to apply several coats of resin and eventually the cracks filled in.

### Physical build: If it ain't broke... don't fix it 

<img src="/images/silverWire.jpeg" width="600"/>

I didn't put a lot of time, effort or energy into modifying the physical build. I have some ideas floating around, but I'd want to save them for a future build. In either case, I had this cool mirrored skull bottle to work with. 

<img src="/images/silverLightTest.gif" width="600"/>

The second I connected the battery to the lights I knew that the mirrored glass would add a really cool effect. I thought the additional levels of reflection, diffusion, and discoloration would really pay off in the final implementation.

<img src="/images/silverHole-1.jpeg" width="250"/> <img src="/images/silverHole-2.jpeg" width="250"/> <img src="/images/silverHole-3.jpeg" width="250"/>

Every time I talk to people about the skull, I tell them that the hardest thing about the project is drilling the hole in the bottle. I feel like Im getting better at it, but still experimenting with "better." This year I attempted to use a dremel and a sanding / polishing tip to smooth out the hole. It did not, rather the I broke the tip off in the existing hole. I eventually pulled out the tip with a needle nosed pliars. 

<img src="/images/silverPreResin.jpeg" width="600"/>

With all that out of the way, I was ready to start the resin...

# The Resin

<img src="/images/silverPour.jpeg" width="600"/>

I used resin from Resin Obsession again and it was super consistent. I added mica powder for extra diffusion. I didn't think to take a picture, but I will say that I am getitng much better at caulking the power wire hole. Not a single drop spilled this year.

<img src="/images/silverLit-0.jpeg" width="600"/>

The quality of light diffusion and reflection was evident from the first pour. 

<img src="/images/silverLit-1.gif" width="300"/> <img src="/images/silverLit-2.gif" width="300"/>

As I added more resin the effect just kept getting better. The skull took on a really spooky glow depending on which light mode you went through. (These pictures all show the new mode for this year: Multi-color blink fade)

<img src="/images/silverLit-3.gif" width="300"/> <img src="/images/silverLit-4.gif" width="300"/>

More deffusion, more awesome...

<img src="/images/silverOff.gif" width="600"/>

When it's off, it's pretty difficult to discern that there are electronics in there.

# The software
I did want to add something new with this version and software seemed to be the easiest thing to change. 

- [Updated the `blinkFade()` function](https://github.com/icejester/canada-day-skull/blob/998edcdd4510581338fc247088385522c4c4145c/main.py#L95) to require a color rather than forcing 'white' on myself every time.
- [Added a COLORPALLET](https://github.com/icejester/canada-day-skull/blob/998edcdd4510581338fc247088385522c4c4145c/main.py#L33) to allow for a collection of related colors.
- [Hacky garbage](https://github.com/icejester/canada-day-skull/blob/998edcdd4510581338fc247088385522c4c4145c/main.py#L179) to pass a random color from a pallet to the function. 