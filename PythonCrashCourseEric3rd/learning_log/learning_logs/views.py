from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


# Create your views here.
# the request is the request parmater from the user ex ../index.html. Django begins from urls.py and comes
# here and executes this function
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html') #It takes the request object and what to show to the user

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added') # We query the database table Topic items
    context = {'topics': topics} # We create a dictionary
    # print(context['topics'][0])
    return render(request, 'learning_logs/topics.html', context) #We render the template by sending the dictionary info and then html can use a for loop to iterate the topics key array
# When building a page that uses data, we call
# render() with the request object, the template we want to use, and the
# context dictionary

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # Get specific topic
    entries = topic.entry_set.order_by('-date_added') # Get the entry lower case class object, minus in date means reversed
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    # We use get to read from server and post to submit information
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST) #Create a form object
        if form.is_valid(): # Validate it based on database, and check if all fields are completed
            form.save() #Save it (write the data to database directly. The mapping is auto
            return redirect('learning_logs:topics') #redirect the user to the topics
    # Display a blank or invalid form if it is get request.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

