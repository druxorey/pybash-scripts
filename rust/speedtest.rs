use std::time::Instant;

fn main() {
    let start = Instant::now();

    let mut count = 0;
    let number = 50_000_000;

    for _i in 0..number {
        count += 1;
    }

    let duration = start.elapsed();

    println!("Counting to {} in Rust took {:?} ms.", number, duration.as_millis());
}
