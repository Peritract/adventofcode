use std::fs;
use std::fmt;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

#[derive(Debug)]
#[derive(Clone)]
struct Point(i32, i32);

impl fmt::Display for Point {

    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {

        write!(f, "({},{})", self.0, self.1)
    }
}

fn get_valid_neighbours(point:&Point, w:i32, h:i32) -> Vec<Point> {
  
  let mut neighbours = Vec::new();
  
  for d in [(0, 1), (0, -1), (1, 1), (1, 0),
            (1, -1), (-1, 1), (-1, 0), (-1, -1)] {
    let new = (point.0 + d.0, point.1 + d.1);

    if new.0 >= 0 && new.1 >= 0 && new.0 < w && new.1 < h {
      neighbours.push(Point(new.0, new.1));
    }
  }
  
  return neighbours;
}

struct Octopus{
  loc:Point,
  state:i32,
  flashed: bool,
  neighbours:Vec<Point>
}

impl Octopus {
  fn new(loc:Point, state:i32, flashed:bool, width:i32, height:i32) -> Self {

    let neighbours:Vec<Point> = get_valid_neighbours(&loc, width, height);

    Self {loc:loc, state:state, flashed:flashed, neighbours:neighbours}
  }

  fn reset(&mut self) {
    if self.state > 9 {
      self.state = 0;
    }
    self.flashed = false;
  }

  fn increment(&mut self) {
    self.state += 1;
  }

  fn get_neighbours(&self) -> Vec<Point> {
    let mut new_neighbours:Vec<Point> = Vec::new();

    for p in &self.neighbours {
      new_neighbours.push(p.clone());
    }

    return new_neighbours;
  }

  fn flash(&mut self) -> bool {
    if (!self.flashed) && (self.state > 9) {
      self.flashed = true;
      
      return true;
    }
    return false;
  }
}

impl fmt::Display for Octopus {

    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {

        write!(f, "({}, {}, {})", self.loc, self.state, self.flashed)
    }
}

fn display_grid(grid: &Vec<Vec<Octopus>>) {
  let width = grid[0].len();
  let height = grid.len();
  for y in 0..height {
    let mut row:String = String::new();
    for x in 0..width {
      row += &grid[y][x].state.to_string();
    }
    println!("{}", row);
  }
}

fn create_octopus_grid(data:&String) -> Vec<Vec<Octopus>> {
  let lines:Vec<&str> = data.split("\n").collect();
  let width = lines[0].len() as i32;
  let height = lines.len() as i32;

  let mut grid:Vec<Vec<Octopus>> = Vec::new();

    for y in 0..height {
      let mut row:Vec<Octopus> = Vec::new();
      for x in 0..width {
        let state = lines[y as usize].chars().nth(x as usize).unwrap();
        row.push(Octopus::new(Point(y, x), state.to_digit(10).unwrap() as i32, false, width, height))
      }
      grid.push(row);
    }

    return grid;
  }

  fn first_star(data:&String) -> i32 {
    
    let mut grid = create_octopus_grid(data);
    let width = grid[0].len();
    let height = grid.len();
    let mut flashes = 0;

    for _step in 1..101 {

      // Increment
      for y in 0..height {
        for x in 0..width {
          grid[y][x].increment();
        }
      }

      // Flash
      let mut flash = true;
      while flash == true {
        flash = false;
        for y in 0..height {
          for x in 0..width {
            let check = grid[y][x].flash();
            if check {
              for oc in grid[y][x].get_neighbours() {
                grid[oc.0 as usize][oc.1 as usize].increment();

              }
              flashes += 1;
              flash = true;
            }
          }
        }
      }

      // Reset
      for y in 0..height {
        for x in 0..width {
          grid[y][x].reset();
        }
      }
  }

  return flashes;
}

fn second_star(data:&String) -> i32 {
  let mut grid = create_octopus_grid(data);
    let width = grid[0].len();
    let height = grid.len();
    let mut step = 0;
    let mut all = false;

    while !all {
      step += 1;

      // Increment
      for y in 0..height {
        for x in 0..width {
          grid[y][x].increment();
        }
      }

      // Flash
      let mut flash = true;
      while flash == true {
        flash = false;
        for y in 0..height {
          for x in 0..width {
            let check = grid[y][x].flash();
            if check {
              for oc in grid[y][x].get_neighbours() {
                grid[oc.0 as usize][oc.1 as usize].increment();

              }
              flash = true;
            }
          }
        }
      }

      // Reset
      for y in 0..height {
        for x in 0..width {
          grid[y][x].reset();
        }
      }

      // Check
      all = true;
      for y in 0..height {
        for x in 0..width {
          if grid[y][x].state != 0 {
            all = false;
          }
        }
      }

  }

  return step;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
