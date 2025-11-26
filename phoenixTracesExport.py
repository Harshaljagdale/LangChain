# Exporting traces to Phoenix Cloud

import os
from phoenix.otel import register
from dotenv import load_dotenv


load_dotenv()


# Ensure environment variables are set here or in your shell/deployment config

# Register the Phoenix Tracer Provider
# project_name can be specified here or via the PHOENIX_PROJECT_NAME env var
tracer_provider = register(
    project_name="OpenAI",
    auto_instrument=True  # Automatically trace supported libraries (e.g., OpenAI)
)

# Your application code goes here. Any instrumented code will now 
# send traces to your Phoenix Cloud instance.

# Example of manual instrumentation (if needed):
tracer = tracer_provider.get_tracer(__name__)
with tracer.start_as_current_span("my-cloud-task") as span:
    # Do work...
    span.set_attribute("data.size", 100)
    print("Trace data being exported to Phoenix Cloud...")

# In a production application, you should explicitly shut down the provider 
# before the process exits to ensure all buffered traces are sent.
tracer_provider.shutdown()