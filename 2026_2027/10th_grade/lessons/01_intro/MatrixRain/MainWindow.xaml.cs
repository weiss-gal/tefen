using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Threading;

namespace MatrixRain
{
    public partial class MainWindow : Window
    {
        private const double CharFontSize = 18;
        private const double CharWidth = 13;
        private const double CharHeight = 20;
        private const int TrailLength = 20;
        private const double TickIntervalMs = 40;
        private const double FlickerChance = 0.02;

        private readonly Random random = new Random();
        private readonly DispatcherTimer timer = new DispatcherTimer();

        private int columns;
        private int rows;
        private TextBlock[,] cells;
        private char[,] chars;
        private double[] headRow;
        private double[] speed;
        private Brush headBrush;
        private Brush[] trailBrushes;

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            BuildBrushes();
            BuildGrid();

            // Render one frame immediately so the screen isn't blank
            // for the first TickIntervalMs before the timer fires.
            Timer_Tick(this, EventArgs.Empty);

            timer.Interval = TimeSpan.FromMilliseconds(TickIntervalMs);
            timer.Tick += Timer_Tick;
            timer.Start();
        }

        private void BuildBrushes()
        {
            headBrush = CreateBrush(Color.FromRgb(210, 255, 210));

            trailBrushes = new Brush[TrailLength];
            for (int j = 0; j < TrailLength; j++)
            {
                double t = (double)j / TrailLength; // 0 near the head .. 1 near the tail
                byte green = (byte)(255 - t * 155);
                byte glow = (byte)(60 * (1 - t));
                trailBrushes[j] = CreateBrush(Color.FromRgb(glow, green, glow));
            }
        }

        private static Brush CreateBrush(Color color)
        {
            var brush = new SolidColorBrush(color);
            brush.Freeze();
            return brush;
        }

        private void BuildGrid()
        {
            columns = Math.Max(1, (int)(MainCanvas.ActualWidth / CharWidth));
            rows = Math.Max(1, (int)(MainCanvas.ActualHeight / CharHeight));

            cells = new TextBlock[columns, TrailLength];
            chars = new char[columns, TrailLength];
            headRow = new double[columns];
            speed = new double[columns];

            for (int col = 0; col < columns; col++)
            {
                for (int j = 0; j < TrailLength; j++)
                {
                    var textBlock = new TextBlock
                    {
                        FontFamily = new FontFamily("Consolas"),
                        FontSize = CharFontSize,
                        Opacity = 0
                    };
                    Canvas.SetLeft(textBlock, col * CharWidth);
                    cells[col, j] = textBlock;
                    MainCanvas.Children.Add(textBlock);
                }

                ResetColumn(col, startOnScreen: true);
            }
        }

        private void ResetColumn(int col, bool startOnScreen)
        {
            speed[col] = random.NextDouble() * 0.9 + 0.4;
            headRow[col] = startOnScreen
                ? random.NextDouble() * rows
                : -random.NextDouble() * 30;

            for (int j = 0; j < TrailLength; j++)
            {
                chars[col, j] = RandomChar();
            }
        }

        private char RandomChar()
        {
            if (random.NextDouble() < 0.15)
            {
                return (char)('0' + random.Next(10));
            }

            // Half-width katakana block - the classic "Matrix" look.
            return (char)(0x30A0 + random.Next(96));
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            for (int col = 0; col < columns; col++)
            {
                headRow[col] += speed[col];

                if (headRow[col] - TrailLength > rows)
                {
                    ResetColumn(col, startOnScreen: false);
                }

                for (int j = 0; j < TrailLength; j++)
                {
                    double row = headRow[col] - j;
                    TextBlock textBlock = cells[col, j];

                    if (row < 0 || row > rows)
                    {
                        textBlock.Opacity = 0;
                        continue;
                    }

                    Canvas.SetTop(textBlock, row * CharHeight);

                    if (j == 0)
                    {
                        chars[col, j] = RandomChar();
                        textBlock.Foreground = headBrush;
                        textBlock.Opacity = 1;
                    }
                    else
                    {
                        if (random.NextDouble() < FlickerChance)
                        {
                            chars[col, j] = RandomChar();
                        }

                        textBlock.Foreground = trailBrushes[j];
                        textBlock.Opacity = Math.Pow(1 - (double)j / TrailLength, 1.5);
                    }

                    textBlock.Text = chars[col, j].ToString();
                }
            }
        }

        private void Window_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Escape)
            {
                Close();
            }
        }
    }
}
