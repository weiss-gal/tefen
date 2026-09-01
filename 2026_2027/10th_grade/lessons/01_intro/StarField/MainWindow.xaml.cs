using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace StarField
{
    public partial class MainWindow : Window
    {
        private const int StarCount = 600;
        private const double MaxDepth = 800;
        private const double Speed = 2.5;

        // Realistic star colors, weighted like real stellar populations:
        // mostly white / warm-white, with rarer blue-hot and red-cool stars.
        private static readonly (Color Color, double Weight)[] StarPalette =
        {
            (Color.FromRgb(202, 215, 255), 0.12), // blue-white (hot)
            (Colors.White, 0.45),
            (Color.FromRgb(255, 244, 234), 0.20), // warm white
            (Color.FromRgb(255, 210, 161), 0.13), // yellow-orange
            (Color.FromRgb(255, 163, 115), 0.07), // orange
            (Color.FromRgb(255, 120, 120), 0.03), // red
        };

        private readonly Star[] stars = new Star[StarCount];
        private readonly Ellipse[] starShapes = new Ellipse[StarCount];
        private readonly Random random = new Random();
        private readonly DispatcherTimer timer = new DispatcherTimer();

        public MainWindow()
        {
            InitializeComponent();
            InitializeStars();

            timer.Interval = TimeSpan.FromMilliseconds(16);
            timer.Tick += Timer_Tick;
            timer.Start();
        }

        private void InitializeStars()
        {
            for (int i = 0; i < StarCount; i++)
            {
                stars[i] = CreateStar(randomizeDepth: true);

                var ellipse = new Ellipse { Fill = CreateBrush(stars[i].Color) };
                starShapes[i] = ellipse;
                MainCanvas.Children.Add(ellipse);
            }
        }

        private Star CreateStar(bool randomizeDepth)
        {
            return new Star
            {
                X = random.NextDouble() * 2 - 1,
                Y = random.NextDouble() * 2 - 1,
                Z = randomizeDepth ? random.NextDouble() * MaxDepth + 1 : MaxDepth,
                Color = PickStarColor(),
                Brightness = random.NextDouble() * 0.3 + 0.7 // subtle per-star variation
            };
        }

        private Color PickStarColor()
        {
            double r = random.NextDouble();
            double cumulative = 0;

            foreach (var (color, weight) in StarPalette)
            {
                cumulative += weight;
                if (r <= cumulative)
                {
                    return color;
                }
            }

            return Colors.White;
        }

        private static Brush CreateBrush(Color color)
        {
            var brush = new SolidColorBrush(color);
            brush.Freeze();
            return brush;
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            double centerX = MainCanvas.ActualWidth / 2;
            double centerY = MainCanvas.ActualHeight / 2;

            for (int i = 0; i < StarCount; i++)
            {
                Star star = stars[i];
                star.Z -= Speed;

                if (star.Z <= 1)
                {
                    star = CreateStar(randomizeDepth: false);
                    stars[i] = star;
                    starShapes[i].Fill = CreateBrush(star.Color);
                }

                // Perspective projection: stars closer to the camera (small Z)
                // spread further from the screen center and appear bigger/brighter.
                double screenX = centerX + (star.X / star.Z) * centerX;
                double screenY = centerY + (star.Y / star.Z) * centerY;
                double depthFactor = 1 - star.Z / MaxDepth;
                double size = depthFactor * 4 + 0.5;

                Ellipse ellipse = starShapes[i];
                ellipse.Width = size;
                ellipse.Height = size;
                ellipse.Opacity = Math.Min(1, (depthFactor * 0.8 + 0.2) * star.Brightness);
                Canvas.SetLeft(ellipse, screenX);
                Canvas.SetTop(ellipse, screenY);
            }
        }

        private void Window_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Escape)
            {
                Close();
            }
        }

        private class Star
        {
            public double X;
            public double Y;
            public double Z;
            public Color Color;
            public double Brightness;
        }
    }
}
