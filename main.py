from random import randint
from flask import Flask, render_template

app = Flask(
  __name__,
  template_folder = 'templates',
  static_folder = 'static'
)

@app.route('/')
def index():
  message = "Hello RPS!"
  
  
  return render_template(
    'index.html',
    output = message
)
@app.route('/rock')
def rock():
  options = ('Rock', 'Paper', 'Scissor')
  opponent = options[randint(0,len(options)-1)]
  
  if opponent == 'Scissor':
    message = 'You Win, opponent had', opponent
    bs_class = "secondary"
    return render_template(
    'rock.html',
    output = message,
    color = bs_class)
    
  if opponent == 'Paper':
    message = "You Lose! opponent had", opponent
    bs_class = "secondary"
    return render_template(
    'rock.html',
    output = message,
    color = bs_class)
    
  if opponent == 'Rock':
    message = "You Tied! opponent had", opponent
    bs_class = "secondary"
    return render_template(
    'rock.html',
    output = message,
    color = bs_class
)
@app.route('/paper')
def paper():
  options = ('Rock', 'Paper', 'Scissor')
  opponent = options[randint(0,len(options)-1)]
  
  if opponent == 'Rock':
    message = "You Win! Opponent had", opponent
    bs_class = "Primary"
    return render_template(
      'paper.html',
      output = message,
      color = bs_class)
    
  if opponent == 'Paper':
    message = "You Tied! Opponent had", opponent
    bs_class = "primary"
    return render_template(
      'paper.html',
      output = message,
      color = bs_class)
  
  if opponent == 'Scissor':
    message = "You Lose! Opponent had", opponent
    bs_class = "primary"
    return render_template(
      'paper.html',
      output = message,
      color = bs_class
)
@app.route('/scissor')
def scissor():
  options = ('Rock', 'Paper', 'Scissor')
  opponent = options[randint(0,len(options)-1)]
  if opponent == 'Paper':
    message = "You Win! Opponent had", opponent 
    bs_class = "warning"
    return render_template(
      'scissor.html',
      output = message,
      color = bs_class)
  if opponent == 'Rock':
    message = "You Lose! Opponent had", opponent 
    bs_class = "warning"
    return render_template(
      'scissor.html',
      output = message,
      color = bs_class)
  if opponent == 'Scissor':
    message = "You Tied! Opponent had", opponent 
    bs_class = "warning"
    return render_template(
      'scissor.html',
      output = message,
      color = bs_class
)

app.run(
  
  host = "0.0.0.0",
  port = 8080,
  debug = True
)