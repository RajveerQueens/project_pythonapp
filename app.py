import gradio as gr
import time

def bin_search_graphical(sorted_array_str, target_str):
    """
    Performs binary search and yields visual steps in Markdown format.
    """
    try:
        arr = [int(x.strip()) for x in sorted_array_str.split(',')]
        target = int(target_str)
        arr.sort() # sort method to Ensure the array is sorted

        low = 0
        high = len(arr) - 1
        steps = []
        found = False

        while low <= high:
            mid = (low + high) // 2
            
            # Create a visual representation for the current step
            visual_step = []
            for i, val in enumerate(arr):
                if i == mid:
                    visual_step.append(f"**[{val}]**") # Highlight mid in bold
                elif low <= i <= high:
                    visual_step.append(f"`{val}`") # Highlight current search range
                else:
                    visual_step.append(f"{val}") # Other elements

            step_text = f"**Low:** {low}, **High:** {high}, **Mid:** {mid}. Array: {' '.join(visual_step)}"
            
            if arr[mid] == target:
                step_text += f"\n\n**Target {target} found at index {mid}!**"
                steps.append(step_text)
                found = True
                break
            elif arr[mid] < target:
                step_text += f"\nTarget > Mid, moving low to {mid + 1}."
                low = mid + 1
            else:
                step_text += f"\nTarget < Mid, moving high to {mid - 1}."
                high = mid - 1
            
            steps.append(step_text)
            time.sleep(0.5) # Add a small delay for visualization effect

        if not found:
            steps.append(f"\n\n**Target {target} not found in the array.**")

        # Use markdown to format the output
        return "\n\n---\n\n".join(steps)

    except ValueError:
        return "Please enter a valid comma-separated list of numbers and a valid target number."

# Define the Gradio interface
application = gr.Interface(
    fn=bin_search_graphical,
    inputs=[
        gr.Textbox(label="Enter sorted numbers (comma-separated)"),
        gr.Textbox(label="Enter target number")
    ],
    outputs=gr.Markdown(label="Visualization Steps"),
    title="Binary Search Graphical",
    description="Graphically Explain the steps of the binary search algorithm. Input array should ideally be sorted for correct logic."
)

application.launch()
