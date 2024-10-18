# Trò chơi Tetris kết hợp AI sử dụng Thuật toán Di truyền

Dự án này triển khai trò chơi Tetris với AI sử dụng thuật toán di truyền thực hiện. AI sẽ tiến hóa theo thời gian để cải thiện khả năng chơi Tetris một cách tối ưu.

## Mục lục

- [Giới thiệu](#Giới-thiệu)
- [Tính năng](#Tính-năng)
- [Cài đặt](#Cài-đặt)
- [Sử dụng](#Sử-dụng)
- [Thuật toán di truyền](#Thuật-toán-di-truyền)

## Giới thiệu

Dự án Trò chơi Tetris kết hợp AI là sự hòa trộn hoàn hảo giữa trò chơi cổ điển Tetris và trí tuệ nhân tạo. AI học cách chơi Tetris bằng cách tiến hóa một tập hợp các chiến lược thông qua thuật toán di truyền.

## Tính năng

- Lối chơi Tetris cổ điển.
- Người chơi AI được điều khiển bởi thuật toán di truyền.
- Chiến lược tiến hóa cho lối chơi tối ưu.
- Giao diện tương tác và hình ảnh hấp dẫn.

## Cài đặt

1. Clone the repository:

   ```bash
   git clone https://github.com/lapdzvl/Genetic-Algoritm
   cd Tetris-ga
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the trainning program:

   ```bash
   python main.py
   ```

4. Run the game:

   ```bash
   python game.py
   ```

## Sử dụng

- Sử dụng các phím mũi tên để di chuyển và xoay các mảnh Tetris.
- Xem người chơi AI tiến hóa và cải thiện theo thời gian.
- Thưởng thức trò chơi hoặc để AI chơi thay bạn!

## Thuật toán di truyền

Thuật toán di truyền hoạt động bằng cách tiến hóa một tập hợp các chiến lược để chơi Tetris. Mỗi chiến lược được biểu diễn dưới dạng một tập hợp các gen và những chiến lược phù hợp nhất sẽ được chọn để tái sản xuất qua mỗi thế hệ. Theo thời gian, người chơi AI học cách đưa ra quyết định tốt hơn và đạt điểm số cao hơn.
