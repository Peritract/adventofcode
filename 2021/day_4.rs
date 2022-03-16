use std::fs;
use regex::Regex;

fn load_data(filepath:&str) -> String {
  let file = fs::read_to_string(filepath);
  if file.is_ok() {
    return file.unwrap();
  }
  panic!("File not found or unreadable");
  }

fn parse_board(data: &str) -> Vec<Vec<i32>> {

  let re = Regex::new(r" +").unwrap();

  let board:Vec<Vec<i32>> = data.split('\n').map(|line| re.split(line.trim()).map(|x| x.trim().parse::<i32>().unwrap()).collect()).collect();

  return board;
}

fn parse_bingo(data:&str) -> (Vec<i32>, Vec<Vec<Vec<i32>>>) {
  let re = Regex::new(r"\n{2}").unwrap();
  let chunks:Vec<&str> = re.split(data).collect();

  let nums:Vec<i32> = chunks[0].split(",").map(|x| x.parse::<i32>().unwrap()).collect();

  let boards:Vec<Vec<Vec<i32>>> = chunks[1..].into_iter().map(|chunk| parse_board(&chunk)).collect();

  return (nums, boards);
}

fn is_bingo(board:&Vec<Vec<i32>>, nums:&Vec<i32>) -> bool {

  for row in board {
    if row.into_iter().filter(|val| {return nums.contains(val)}).collect::<Vec<&i32>>().len() == row.len() {
      return true;
    };
  }

  for y in 0..board[0].len() {
    let mut valid = true;
    for x in 0..board.len() {
      if !nums.contains(&board[x][y]) {
        valid = false;
      }
    }
    if valid {
      return true;
    }
  }

  return false;
}

fn get_score(board:&Vec<Vec<i32>>, nums:&Vec<i32>) -> i32 {

  let mut total = 0;

  for row in board {
    for val in row {
      if !nums.contains(val) {
        total += val;
      }
    }
  }

  return nums[nums.len() - 1] * total;
}

fn first_star(data:&String) -> i32 {
  
  let (nums, boards) = parse_bingo(data);

  for i in 0..nums.len() {
    let borrowed_nums = &nums[0..i].to_vec();
    for board in &boards {
      if is_bingo(&board, &borrowed_nums) {
        return get_score(&board, &borrowed_nums);
      }
    }
  }

  return 0;
}

fn second_star(data:&String) -> i32 {

  let (nums, boards) = parse_bingo(data);

  let mut new_boards = boards.clone();

  for i in 0..nums.len() {
    let borrowed_nums = &nums[0..i].to_vec();
    if new_boards.len() == 1 {
      if is_bingo(&new_boards[0], &borrowed_nums) {
        return get_score(&new_boards[0], &borrowed_nums);
      }
    }
    new_boards = new_boards.into_iter().filter(|board| !is_bingo(&board, &borrowed_nums)).collect::<Vec<Vec<Vec<i32>>>>();
  }

  return 0;
  
}

fn main() {
  let data = load_data("input.txt");
  println!("First star: {}", first_star(&data));
  println!("Second star: {}", second_star(&data));
}
