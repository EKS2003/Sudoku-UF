if self.selected:
    pygame.draw.rect(self.screen, (255, 0, 0), (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                     2)
else:
    pygame.draw.rect(self.screen, (0, 0, 0), (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

if self.value != 0:
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render(str(self.value), True, (0, 0, 0))
    self.screen.blit(text, (self.col * CELL_SIZE + CELL_SIZE / 2 - text.get_width() / 2,
                            self.row * CELL_SIZE + CELL_SIZE / 2 - text.get_height() / 2))

if self.sketched_value != 0:
    # Handle sketched value drawing here (add your code)
    pass