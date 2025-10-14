from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# creating schema
class Review(BaseModel):
    key_themes: list[str]=Field(description="Write down all the key themes discussed in the review")
    summary: str=Field(description="A short 1-sentence summary of the review")
    sentiment: str=Field(description="Overall sentiment: positive, neutral, or negative")
    pros:Optional[list[str]]=Field(description="Write down all the pros inside the list")
    cons:Optional[list[str]]=Field(description="Write down all the cons inside the list")

annotated_structured_model = model.with_structured_output(Review)

annotatedResult = annotated_structured_model.invoke("""I’ve been using the NovaBrew Elite Smart Coffee Maker for about two months now, and it’s honestly one of the most convenient additions to my kitchen. I used to rely on a basic drip machine, but this one has changed my morning routine completely. The smart app integration lets me schedule brews from bed, adjust coffee strength, and even set a “wake-up brew” alarm so the machine starts automatically before I’m out of bed.

The build quality feels premium — brushed stainless steel body, smooth touchscreen, and the water tank detaches easily for refilling. I really like the reusable mesh filter; it saves me from constantly buying paper ones. The temperature control is accurate, and the coffee always comes out hot but not scalding.

That said, it’s not perfect. The companion app is a bit buggy — sometimes it loses Wi-Fi connection and fails to sync settings. Also, the machine is somewhat noisy during brewing, especially when grinding beans. The grinder itself is good, but it takes a bit of experimenting to get the grind size right for your preferred strength.

I’d still recommend it to anyone who wants a coffee maker that balances smart features with solid brewing performance. It’s not cheap, but if you’re into tech and coffee, it feels worth the investment.

Pros:

Excellent build quality with stainless steel finish

App integration for scheduling and customization

Reusable filter saves money and reduces waste

Adjustable brew strength and temperature control

Consistently hot, flavorful coffee

Cons:

App occasionally disconnects or lags

A bit noisy during grinding and brewing

Slight learning curve for grind size adjustment

Price is on the higher side""")

print(annotatedResult)
print(annotatedResult.summary)
print(annotatedResult.sentiment)