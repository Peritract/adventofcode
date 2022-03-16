use std::fs;
use std::fmt;
use std::cmp;
use std::collections::HashMap;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

struct Point {
  x: i32,
  y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}, {}", self.x, self.y)
    }
}

struct Line {
  start: Point,
  end: Point,
  cat: char,
}

impl fmt::Display for Line {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}, {} -> {}, {} ({})", self.start.x, self.start.y, self.end.x, self.end.y, self.cat)
    }
}

impl Line {
  fn new(raw:&str) -> Self {
    let chunks:Vec<Vec<i32>> = raw.split(" -> ").map(|p| p.split(",").map(|c| c.parse::<i32>().unwrap()).collect()).collect();
    let mut cat = 'o';
    if chunks[0][0] == chunks[1][0] {
      cat = 'v';
    } else if chunks[0][1] == chunks[1][1] {
      cat = 'h';
    }
    Self { start:Point{x:chunks[0][0], y:chunks[0][1]},
           end:Point{x:chunks[1][0], y:chunks[1][1]},
           cat }
  }

  fn get_covered_points(&self) -> Vec<Point> {
    let mut points:Vec<Point> = Vec::new();

    if self.cat != 'o' {

      let start_x = cmp::min(self.start.x, self.end.x);
      let start_y = cmp::min(self.start.y, self.end.y);
      let end_x = cmp::max(self.start.x, self.end.x) + 1;
      let end_y = cmp::max(self.start.y, self.end.y) + 1;

      for x in start_x..end_x {
        for y in start_y..end_y {
          points.push(Point{x:x, y:y});
        }
      }
    } else {
      let mut x = self.start.x;
      let mut y = self.start.y;

      while x != self.end.x || y != self.end.y {
        points.push(Point{x:x, y:y});
        if x < self.end.x {
          x += 1;
        } else if x > self.end.x {
          x -= 1;
        }
        if y < self.end.y {
          y += 1;
        } else if y > self.end.y {
          y -= 1;
        }
      }
      points.push(Point{x: self.end.x, y:self.end.y});
    }

    return points;
  }
}

fn get_lines(data:&str) -> Vec<Line> {
  let mut lines:Vec<Line> = Vec::new();

  for text_line in data.split("\n") {
    lines.push(Line::new(text_line));
  }

  return lines;

}

fn first_star(data:&str) -> i32 {

  let lines:Vec<Line> = get_lines(data);
  let mut squares:HashMap<String, i32> = HashMap::new();

  for l in lines {
    if l.cat != 'o' {
      for c_p in l.get_covered_points() {
        let stat = squares.entry(format!("{}, {}", c_p.x, c_p.y)).or_insert(0);
        *stat += 1;
      }
    }
  }

  let mut count = 0;
  for (_k, v) in squares {
    if v > 1 {
      count += 1;
    }
  }

  return count;
}

fn second_star(data:&str) -> i32 {
  let lines:Vec<Line> = get_lines(data);
  let mut squares:HashMap<String, i32> = HashMap::new();

  for l in lines {
    for c_p in l.get_covered_points() {
      let stat = squares.entry(format!("{}, {}", c_p.x, c_p.y)).or_insert(0);
      *stat += 1;
    }
  }

  let mut count = 0;
  for (_k, v) in squares {
    if v > 1 {
      count += 1;
    }
  }

  return count;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
