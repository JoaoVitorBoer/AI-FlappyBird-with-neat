import pygame
import neat
from Models.Bird import Bird
from Models.Pipe import Pipe
from Models.Base import Base

ai_playing = True
generation = 0
pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 50)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load('imgs/bg.png'))

def draw_screen(screen, birds, pipes, base, points, generation):
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    score_text = SCORE_FONT.render(f"Score: {points}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH - 10 - score_text.get_width(), 10))
    generation_text = SCORE_FONT.render(f"Generation: {generation}", True, (255, 255, 255))
    screen.blit(generation_text, (10, 10))
    base.draw(screen)
    pygame.display.update()

def main(genomes, config):
    global generation
    generation += 1
    networks = []
    genome_list = []
    birds = []
    for _, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        genome.fitness = 0
        genome_list.append(genome)
        birds.append(Bird(230, 350))
    base = Base(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    points = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > (pipes[0].x + pipes[0].TOP_PIPE.get_width()):
                pipe_index = 1
        else:
            running = False
            break
        for i, bird in enumerate(birds):
            bird.move()
            genome_list[i].fitness += 0.1
            output = networks[i].activate((bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].bottom)))
            if output[0] > 0.5:
                bird.jump()
        base.move()
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                    if ai_playing:
                        genome_list[i].fitness -= 1
                        genome_list.pop(i)
                        networks.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.TOP_PIPE.get_width() < 0:
                remove_pipes.append(pipe)
        if add_pipe:
            points += 1
            pipes.append(Pipe(600))
            for genome in genome_list:
                genome.fitness += 5
        for pipe in remove_pipes:
            pipes.remove(pipe)
        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > base.y or bird.y < 0:
                birds.pop(i)
                if ai_playing:
                    genome_list.pop(i)
                    networks.pop(i)
        draw_screen(screen, birds, pipes, base, points, generation)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())
    population.run(main, 50)

if __name__ == '__main__':
    run('config.txt')
