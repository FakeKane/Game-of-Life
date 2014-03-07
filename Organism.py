class Organism(object):  # other classes will extend this class,

    #note that default vars are for a very simple tree
    """
    what the organism is... this will probably
    vary or become useless, but good to have for now
    """
    name = 'tree'

    """
    size of the organism (tiny, small, medium, large, etc)
    perhaps ints would be a better model...
    """
    size = 'medium'

    """
    requires sunlight though... if no sunlight, or no soil, then it dies!
    how to implement?
    """
    foodreq = 0

    """
    how many squares can move to get food (per 'act' cycle)
    """
    speed = 0

    """
    how far reaching it can get food from
    (most will probably be short distance, but trees have long roots)
    """
    radius = 4

    """
    list of things it eats (in this case, no other organisms b/c its a tree)
    """
    foods = []

    """
    whether or not the organism is living:
    we can't just remove dead things, they need to be there and be dead
    """
    alive = True

    def __init__(self, nm, sz, fr, sp, rd, fds, al):
        name = nm
        size = sz
        foodreq = fr
        speed = sp
        radius = rd
        foods = fds
        alive = al
    """
    we may want to have some things initialized as carcasses,
    those are important in real ecosystems...
    """
        
    def act(self):
        #if no food, move to get food
        #if no food in range, die/weaken (unsure)
        #else eat, x% chance to reproduce?
        #if eats enough,chance to grow?
        #measure competition with neighbors?
        print("the tree did a little dance, then it died :(")
    
    #def draw(self):
        #draw a tree/whatever the organism is
