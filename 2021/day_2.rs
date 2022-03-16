use std::fs;

fn load_data(filepath:&str) -> String {
  return fs::read_to_string(filepath).expect("Error!");
}

struct Position {
  h:i32,
  d:i32
}

struct ComplexPosition {
  h:i32,
  d:i32,
  a:i32,
}

struct Command {
  plane: String,
  distance: i32
}

fn first_star(data:&String) -> i32 {
  let mut pos = Position{h:0, d:0};

  for line in data.split("\n") {
    let cmd: Vec<&str> = line.split(" ").collect();
    let cmd = Command{plane:String::from(cmd[0]),
                      distance: cmd[1].parse().unwrap()};
    if cmd.plane == "forward" {
      pos.h += cmd.distance 
    } else if cmd.plane == "up" {
      pos.d -= cmd.distance
    } else {
      pos.d += cmd.distance
    }
  }

  return pos.h * pos.d;
}

fn second_star(data:&String) -> i32 {
  let mut pos = ComplexPosition{h:0, d:0, a:0};

  for line in data.split("\n") {
    let cmd: Vec<&str> = line.split(" ").collect();
    let cmd = Command{plane:String::from(cmd[0]),
                      distance: cmd[1].parse().unwrap()};
    if cmd.plane == "forward" {
      pos.h += cmd.distance;
      pos.d += pos.a * cmd.distance;
    } else if cmd.plane == "up" {
      pos.a -= cmd.distance;
    } else {
      pos.a += cmd.distance;
    }
  }

  return pos.h * pos.d;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
