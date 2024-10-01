import csv
import json

# Read data from mushra.csv
with open("mushra.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    questions = []
    for index, row in enumerate(reader):
        question = {}
        question["index"] = index
        question["number"] = int(row["num"])
        question["dryReference"] = row["ref_dry"]
        question["wetReference"] = row["ref_wet"]
        question["dryTarget"] = row["tar_dry"]
        # stimuli are pred1, pred2, random_param
        question["stimuli"] = [row["pred1"], row["pred2"], row["random_param"]]
        questions.append(question)

# Build the questions data
questions_data = {"questions": questions}

# Build the HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MUSHRA Test Form</title>
    <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
</head>
<body>

<!-- MUSHRA Test Form -->
<crowd-form answer-format="flatten-objects">
  <h2>Audio Subjective Test</h2>
  <p>
    <strong>Instructions:</strong> 
    First, listen to two reference audio signals (dry and wet) to learn the AFX mapping between them. 
    Then, listen to a dry target audio. Imagine the wet target audio with the AFX mapping applied. 
    How much do the audio signals below resemble the desired wet target audio? 
    Use the sliders below to rate how much the audio is close to the desired wet audio (0 = very poor, 100 = identical to wet reference).
  </p>
  
  <!-- Container for dynamic questions -->
  <div id="questions-container"></div>
  
  <!-- Submit the results -->
  <p>
    <crowd-button>Submit</crowd-button>
  </p>
  
  <!-- Embed JSON Data -->
  <script type="application/json" id="questions-data">
  QUESTIONS_DATA_PLACEHOLDER
  </script>
  
  <!-- JavaScript to Dynamically Generate Questions -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      const dataElement = document.getElementById('questions-data');
      const data = JSON.parse(dataElement.textContent);
      const container = document.getElementById('questions-container');

      data.questions.forEach(question => {
        // Create the question div
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');
        questionDiv.style.border = '2px solid black';
        questionDiv.style.marginBottom = '20px';
        
        const innerDiv = document.createElement('div');
        innerDiv.style.padding = '20px';
        innerDiv.style.backgroundColor = 'lightgray';
        
        // Question number
        const h1 = document.createElement('h1');
        h1.textContent = question.index;
        innerDiv.appendChild(h1);

        // Reference Audio Section
        const refAudioDiv = document.createElement('div');
        refAudioDiv.style.display = 'flex';
        refAudioDiv.style.justifyContent = 'space-between';
        refAudioDiv.style.alignItems = 'center';
        refAudioDiv.style.maxWidth = '800px';
        refAudioDiv.style.marginBottom = '20px';
        
        // Dry Reference
        const dryRefDiv = document.createElement('div');
        dryRefDiv.style.flex = '1';
        dryRefDiv.style.textAlign = 'center';
        dryRefDiv.innerHTML = '<strong>Dry Reference Audio:</strong>';
        const dryRefAudio = document.createElement('audio');
        dryRefAudio.controls = true;
        dryRefAudio.style.width = '100%';
        const dryRefSource = document.createElement('source');
        dryRefSource.src = question.dryReference;
        dryRefSource.type = 'audio/wav';
        dryRefAudio.appendChild(dryRefSource);
        dryRefDiv.appendChild(dryRefAudio);
        
        // Arrow between Dry and Wet References
        const arrowDiv = document.createElement('div');
        arrowDiv.style.flexShrink = '0';
        arrowDiv.style.padding = '0 20px';
        arrowDiv.style.fontSize = '30px';
        arrowDiv.style.textAlign = 'center';
        arrowDiv.innerHTML = '<p>→</p>';

        // Wet Reference
        const wetRefDiv = document.createElement('div');
        wetRefDiv.style.flex = '1';
        wetRefDiv.style.textAlign = 'center';
        wetRefDiv.innerHTML = '<strong>Wet Reference Audio:</strong>';
        const wetRefAudio = document.createElement('audio');
        wetRefAudio.controls = true;
        wetRefAudio.style.width = '100%';
        const wetRefSource = document.createElement('source');
        wetRefSource.src = question.wetReference;
        wetRefSource.type = 'audio/wav';
        wetRefAudio.appendChild(wetRefSource);
        wetRefDiv.appendChild(wetRefAudio);

        refAudioDiv.appendChild(dryRefDiv);
        refAudioDiv.appendChild(arrowDiv);
        refAudioDiv.appendChild(wetRefDiv);
        innerDiv.appendChild(refAudioDiv);
        
        // Dry Target Audio
        const dryTargetDiv = document.createElement('div');
        dryTargetDiv.style.display = 'flex';
        dryTargetDiv.style.justifyContent = 'space-between';
        dryTargetDiv.style.alignItems = 'center';
        dryTargetDiv.style.maxWidth = '800px';
        dryTargetDiv.style.marginBottom = '20px';
        
        const dryTargetAudioDiv = document.createElement('div');
        dryTargetAudioDiv.style.flex = '1';
        dryTargetAudioDiv.style.textAlign = 'center';
        dryTargetAudioDiv.innerHTML = '<strong>Dry Target Audio:</strong>';
        const dryTargetAudio = document.createElement('audio');
        dryTargetAudio.controls = true;
        dryTargetAudio.style.width = '100%';
        const dryTargetSource = document.createElement('source');
        dryTargetSource.src = question.dryTarget;
        dryTargetSource.type = 'audio/wav';
        dryTargetAudio.appendChild(dryTargetSource);
        dryTargetAudioDiv.appendChild(dryTargetAudio);

        // Arrow between Dry Target and Predicted Wet
        const targetArrowDiv = document.createElement('div');
        targetArrowDiv.style.flexShrink = '0';
        targetArrowDiv.style.padding = '0 20px';
        targetArrowDiv.style.fontSize = '30px';
        targetArrowDiv.style.textAlign = 'center';
        targetArrowDiv.innerHTML = '<p>→</p>';

        // Predicted Wet (Placeholder)
        const predictedWetDiv = document.createElement('div');
        predictedWetDiv.style.flex = '1';
        predictedWetDiv.style.textAlign = 'center';
        predictedWetDiv.innerHTML = '<p style="font-size:50px;">?</p>';

        dryTargetDiv.appendChild(dryTargetAudioDiv);
        dryTargetDiv.appendChild(targetArrowDiv);
        dryTargetDiv.appendChild(predictedWetDiv);
        innerDiv.appendChild(dryTargetDiv);

        questionDiv.appendChild(innerDiv);
        
        // Stimuli Section
        const stimuliDiv = document.createElement('div');
        stimuliDiv.style.padding = '10px';
        stimuliDiv.style.backgroundColor = 'beige';

        question.stimuli.forEach((stimulus, index) => {
          const stimulusRowDiv = document.createElement('div');
          stimulusRowDiv.style.display = 'flex';
          stimulusRowDiv.style.alignItems = 'center';
          stimulusRowDiv.style.marginBottom = '20px';

          const stimulusAudioDiv = document.createElement('div');
          stimulusAudioDiv.style.flex = '1';

          const stimulusAudio = document.createElement('audio');
          stimulusAudio.controls = true;
          stimulusAudio.style.width = '100%';
          const stimulusSource = document.createElement('source');
          stimulusSource.src = stimulus;
          stimulusSource.type = 'audio/wav';
          stimulusAudio.appendChild(stimulusSource);

          stimulusAudioDiv.appendChild(stimulusAudio);
          
          const sliderDiv = document.createElement('div');
          sliderDiv.style.flexShrink = '0';
          sliderDiv.style.marginLeft = '20px';
          sliderDiv.style.width = '200px';

          const slider = document.createElement('crowd-slider');
          slider.setAttribute('name', 'audio_sample_' + question.index + '_' + (index + 1) + '_rating');
          slider.setAttribute('min', '0');
          slider.setAttribute('max', '100');
          slider.setAttribute('required', '');
          slider.setAttribute('pin', '');

          sliderDiv.appendChild(slider);
          stimulusRowDiv.appendChild(stimulusAudioDiv);
          stimulusRowDiv.appendChild(sliderDiv);

          stimuliDiv.appendChild(stimulusRowDiv);
        });

        questionDiv.appendChild(stimuliDiv);
        container.appendChild(questionDiv);
      });
    });
  </script>
  
</crowd-form>

</body>
</html>
"""

# Replace the placeholder with the JSON data
html_output = html_template.replace(
    "QUESTIONS_DATA_PLACEHOLDER", json.dumps(questions_data, indent=2)
)

# Write the HTML output to a file
with open("mushra_test.html", "w") as f:
    f.write(html_output)
