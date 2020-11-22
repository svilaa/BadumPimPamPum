# Hackeps2020
# Sergi Vila Almenara
# Triumph: Hero's Journey

def ordinaryWorld():
    Clock.bpm = 144
    Scale.default = "dorian"
    var.chords = var([0,4,5,3],4)
    b2 >> bass(var.chords, dur=[1/2,1/2,1/4])
def call():
    d1 >> play("x-")
def refusal():
    d2 >> play("  * ")
def mentor():
    p2 >> pluck(var.chords, dur=PDur([3,5,7],8))
def threshold():
    b3 >> sawbass([0,-1,3], dur=[4,4,8])
def test():
    p2.stop()
    b2.stop()
    p1 >> star(b3.pitch)
def apotheosis():
    p1 >> star(b3.pitch + (0,2,4))
def noReturn():
    p1 >> star(b3.pitch + (0,2,4), dur=[3/4, 3/4, 1/2])
def ascension():
    b3 >> sawbass([2,3,4,6], dur=4)
def rescue():
    d1.stop()
    d2 >> play("  h ")
def master():
    b3.stop()
    p1 >> star(b3.pitch + (0,2,0), dur=[3/4, 3/4, 1/2])
def freedom():
    p1 >> star(b3.pitch + (0,2,0), dur=[4])
def resolution():
    p1.stop()
def redemption():
    d2.stop()
herosJourney = [[ordinaryWorld, 0], [call, 12], [refusal, 12], [mentor, 12], [threshold, 18],
         [test, 12], [apotheosis, 26], [noReturn, 24], [ascension, 24], [rescue, 28],
         [master, 12], [freedom, 8.5], [resolution, 1], [redemption, 7]]
time = 0
for verse in herosJourney:
    time += verse[1]
    Clock.future(time, verse[0])
    
Clock.clear()
