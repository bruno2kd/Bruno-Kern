import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>BKDFLIX</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
            color: #E50914
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        html, body {
            background-image: url(https://s-media-cache-ak0.pinimg.com/736x/d9/b4/2d/d9b42dc0154ce6fb336a686ab015c6ca--marble-texture-black-marble.jpg);
            background-size: 141px 142px;
            font-family: "Roboto", sans-serif; 
            font-weight: 300; 
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 970px;
        }

        .jumbotron {
            background-color: #000;
            color: #fff;
            height: 650px;
        }

        .jumbotron .navbar-brand {
            color: #E50914;
            padding: 30px;
        }

        .jumbotron li {
          display: inline-block;
          list-style: none;
          padding: 20px;
          color: #E50914;
        }

        .jumbotron a {
          display: inline-block;
          text-decoration: none;
          color: #fff;
        }

        .jumbotron h1 {
          /*margin: 40px auto;*/
          font-size: 58px;
          padding: 50px
        }

        .jumbotron .btn {
          border: 1px solid #fff;
          color: #fff;
          padding: 10px 20px;
          border-radius: 2px;
          background: transparent;
        }

        .jumbotron .main {
          text-align: center;
          color: #E50914;
          padding: 40px 0;
        }

        .jumbrotron p {
            color: #fff;
        }

        .btn:hover {
          background-color: #E50914;
          color: #fff;
          border: 1px solid #E50914
        }

        form {
          margin: 60px;
        }

        #search {
          background: transparent;
          color: #fff;
          border: 0px;
          border-bottom: 1px solid #fff;
          margin: 20px;
          width: 400px;
          font-size: 18px;
        }

        #search:hover {
          border-bottom: 1px solid #E50914;
        }

        #search:focus {
          border: none;
          border-bottom: 1px solid #E50914;
          box-shadow: 0px 0px 0px;
          outline: 0px;
        }

        .btn-default {
            color: #fff;
        }

        .supporting .container {
          padding: 30px;  
        }

        .container h2 {
          text-align: center;
          color: #E50914;
          font-size: 40px;
        }

        .container p {
          text-align: center;
          color: #fff;
          margin-bottom: 50px;
          font-size: 18px;
        }

        .supporting .thumbnail {
          background: transparent;
          border: 0
        }

        .feature {
          background: url(https://cdn.shutterstock.com/shutterstock/videos/15913282/thumb/1.jpg) no-repeat center center;
          background-size: cover;
          height: 400px;
          padding: 150px;
        }

        .footer {
          background-color: #000;
          padding: 80px;
        }

        .footer h3 {
          color: #fff;
          font-size: 18px;
        }

        .footer ul{
          list-style: none;
          color: #E50914;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <div class="jumbotron">
      <div class="container">
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">BKDFLIX</a>
          </div>
          <div class="pull-right">
              <ul>
                <li><a href="#">Login</a></li>
                <li><a href="#" class="btn btn-default">Register</a></li>
              </ul>
            </div>
        </div>
      </div>

        <!--
        <div class="header">
          <div class="row">
            
            <div class="pull-right">
              <ul>
                <li><a href="#">Login</a></li>
                <li><a href="#" class="btn btn-default">Sign Up</a></li>
              </ul>
            </div>
          </div>
        </div>
        -->

        <div class="main">
          <h1>The Best Movie Selection</h1>
          <a class="btn btn-default">Learn More</a>
          <form class="form-inline" role="form">
            <div class="form-group">
            <input class="form-control" placeholder="Find a movie in our catalog" id="search" type="text">
            </div>
            <label class="btn btn-default">Search</label>
          </form>
        </div>
      </div>
    </div>

    <div class="supporting">
      <div class="container">
        <h2>Stream any movie you want</h2>
        <p>Register to watch the full movie</p>
        <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      
    </div>
    <div class="container">
      {movie_tiles}
    </div>
      </div>
    </div>

    <div class="feature">
      <div class="container">
        <h2>Also on your smartphone</h2>
        <p>Watch the movies also on your device</p>
      </div>
    </div>

    <div class="footer">
      <div class="container">
        <div class="row">
          <div class="col-md-3">
            <h3>BKDFLIX</h3>
            <ul>
              <li>How to register</li>
              <li>Condition Terms</li>
              <li>Help</li>
            </ul>
          </div>
          <div class="col-md-3">
            <h3>More About</h3>
            <ul>
              <li>Contact US</li>
              <li>Trailers</li>
            </ul>
          </div>
          <div class="col-md-3 col-md-offset-3">
            <h3>Social</h3>
            <ul>
              <li>Facebook</li>
              <li>Instagram</li>
              <li>Youtube</li>
            </ul>
          </div>
        </div>      
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)