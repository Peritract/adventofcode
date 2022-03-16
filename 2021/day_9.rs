use std::fs;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn first_star(data:&String) -> i32 {
  let grid:Vec<Vec<i32>> = data.split('\n').map(|l| l.split("").filter(|c| c.len() > 0).map(|z| z.parse::<i32>().unwrap()).collect()).collect();

  let mut low:i32 = 0;

  for y in 0..grid.len() {
    for x in 0..grid[y].len() {
      let mut lower:bool = false;
      
      if y >= 1 {
        if grid[y - 1][x] <= grid[y][x] {
          lower = true;
        }
      }
      if y < grid.len() - 1 {
        if grid[y + 1][x] <= grid[y][x] {
          lower = true;
        }
      }
      if x >=  1 {
        if grid[y][x - 1] <= grid[y][x] {
          lower = true;
        }
      }
      if x < grid[y].len() - 1 {
        if grid[y][x + 1] <= grid[y][x] {
          lower = true;
        }
      }

      if !lower {
        low += grid[y][x] + 1;
      }
    }
  } 
  return low;
}

fn get_valid_neighbours(x:usize, y:usize, w:usize, h:usize) -> Vec<Vec<usize>> {
  let mut neighbours = Vec::new();
  
  if y > 0 {
    neighbours.push(vec![y - 1, x]);
  }
  if y < h {
    neighbours.push(vec![y + 1, x]);
  }
  if x > 0 {
    neighbours.push(vec![y, x - 1]);
  }
  if x < w {
    neighbours.push(vec![y, x + 1]);
  }
  
  return neighbours;
}

fn find_basin_size(start:Vec<usize>, grid:&Vec<Vec<i32>>) -> i32 {
  let mut size = 0;
  let mut edge = Vec::new();
  let mut searched = Vec::new();
  let w = grid[0].len() - 1;
  let h = grid.len() - 1;
  edge.push(start);

  while edge.len() > 0 {
    let curr = edge.pop().unwrap();
    searched.push(curr.clone());
    if grid[curr[0]][curr[1]] != 9 {
      size += 1;
      for n in get_valid_neighbours(curr[1], curr[0], w, h) {
        if !edge.contains(&n) && !searched.contains(&n) {
          edge.push(n);
        }
      }
    }
  }

  return size;
}

fn second_star(data:&String) -> i32 {
  let grid:Vec<Vec<i32>> = data.split('\n').map(|l| l.split("").filter(|c| c.len() > 0).map(|z| z.parse::<i32>().unwrap()).collect()).collect();

  let w = grid[0].len() - 1;
  let h = grid.len() - 1;

  let mut basins:Vec<i32> = Vec::new();

  for y in 0..grid.len() {
    for x in 0..grid[0].len() {
      let neighbours = get_valid_neighbours(x, y, w, h);
      let mut lower = false;
      for n in neighbours {
        if grid[n[0]][n[1]] <= grid[y][x]  {
          lower = true;
        }
      }
      if !lower {
        basins.push(find_basin_size(vec![y, x], &grid))
      }
    }
  }
  basins.sort();
  let mut total:i32 = 1;
  for x in basins[basins.len() - 3..basins.len()].iter() {
    total = total * x;
  }
  return total;
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
