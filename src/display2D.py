from sdl2 import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from vec2 import *
from grafo2D import *
from random import seed
from font import *

class display:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        SDL_Init(SDL_INIT_EVERYTHING)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)
        SDL_GL_SetSwapInterval(1)
        self.window = SDL_CreateWindow(b'Fruchterman-Reingold',
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED, 
            self.width, self.height,
            SDL_WINDOW_OPENGL | SDL_WINDOW_SHOWN)

        self.glcontext = SDL_GL_CreateContext(self.window)
       
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glLineWidth(1)
        glClearColor(0.3, 0.3, 0.3, 1.0)

        glMatrixMode(GL_PROJECTION)
        glOrtho(-self.width/2, self.width/2, -self.height/2, self.height/2, -self.height/2, self.height/2)
        glMatrixMode(GL_MODELVIEW)

        seed()

        self.running = False
        self.keys = {}
        self.mouse = vec()
        self.grabed = None

        self.G = graph()

        self.G.load_matrix("data/petersen")
        #self.G.complete(10)
        #self.G.bipartite(3, 6)

        self.G.random(50)

    def grab(self):
        for v in self.G.V:
            if (v.p - self.mouse).norm() < 10:
                self.grabed = v
                break

    def release(self):
        self.grabed = None

    def move_grabed(self):
        if self.grabed != None:
            self.grabed.p = self.mouse

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.render()

    def events(self):
        event = SDL_Event()
        self.mouse_rel = vec()

        while SDL_PollEvent(event) != 0:
            if event.type == SDL_QUIT:
                self.running = False
            if event.type == events.SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_ESCAPE:
                    self.running = False

            if (event.type == SDL_MOUSEMOTION):
                self.mouse = vec(event.motion.x - self.width/2, self.height/2 - event.motion.y)

            if (event.type == SDL_MOUSEBUTTONDOWN):
                if (event.button.button == SDL_BUTTON_LEFT):
                    self.keys["left"] = True
                    self.grab()

                if (event.button.button == SDL_BUTTON_RIGHT):
                    self.keys["right"] = True

            if (event.type == SDL_MOUSEBUTTONUP):
                if (event.button.button == SDL_BUTTON_LEFT):
                    self.keys["left"] = False
                    self.release()

                if (event.button.button == SDL_BUTTON_RIGHT):
                    self.keys["right"] = False

    def update(self):
        self.G.iteration()

        if self.keys.get("left"):
            self.move_grabed()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        self.render_graph(self.G)

        SDL_GL_SwapWindow(self.window)

    def render_graph(self, g):
        glPointSize(5)
        glColor3f(0.8, 0, 0)
        glBegin(GL_POINTS)

        for v in g.V:
            glVertex2f(v.p.x, v.p.y)

        glEnd()
            
        glColor3f(0, 0, 0.1)
        glBegin(GL_LINES)
        
        for e in g.E:
            glVertex2f(e.a.p.x, e.a.p.y)
            glVertex2f(e.b.p.x, e.b.p.y)

        glEnd()

        glPointSize(1)
        glColor3f(1, 1, 1)
        for v in g.V:
            if v.label == "":
                continue

            glPushMatrix()
            
            glTranslatef(v.p.x + 3, v.p.y + 3, 0)
            glScalef(0.2, 0.2, 0.2)
            self.render_string(v.label)

            glPopMatrix()

    def render_string(self, str):
        for c in str:
            ch = Font[ord(c)]
            for i in range(len(ch)-1):
                glBegin(GL_LINE_STRIP)
                for coord in ch[i+1]:
                    glVertex2f(coord[0], coord[1])

                glEnd()
            glTranslatef(ch[0], 0.0, 0.0)

if __name__ == "__main__":
    display = display(900, 710)
    display.run()