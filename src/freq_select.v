/* Generated by Yosys 0.36+42 (git sha1 70d35314d, clang 11.0.1-2 -fPIC -Os) */

module freq_select(clk_1, clk_2, data, freq_out);

  wire [6:0] _0_;
  input [6:0] clk_1;
  wire [6:0] clk_1;
  input [6:0] clk_2;
  wire [6:0] clk_2;
  input data;
  wire data;
  output [6:0] freq_out;
  wire [6:0] freq_out;
  assign _0_ = data ? clk_1 : clk_2;
  assign freq_out = _0_;
endmodule
