# 💡 Inspiration ✨

Embarking on our CalTrack adventure, we were fueled by a vision to revolutionize the way individuals approach their health. We aimed to dismantle the tedious barriers of traditional calorie counting, transforming it from a burdensome task into a delightful, almost effortless daily interaction. It’s where advanced tech seamlessly blends with the essential aspects of nutrition, condensed into the simple act of capturing a photo. We embraced the philosophy that pursuing a wholesome lifestyle should be convenient, straightforward, and completely devoid of stress.

CalTrack emerged as our innovative response to this vision—the ultimate tool to keep wellness not just within reach, but actively engaged in the foreground of our users' lives. We noticed that while other platforms provided pieces to the puzzle, they often fell short with clunky interfaces and tiring manual data entries. CalTrack is designed to bridge that gap, offering a solution that’s intuitive and as natural as taking a selfie.

# 🍎 What it does 🥗

Enter the world of CalTrack, where sophisticated computer vision meets artificial intelligence to create a seamless meal identification experience. Forget the cumbersome process of scouring through endless food lists to painstakingly log every bite. No more dealing with complex user interfaces, searching through databases, and manual logging. With CalTrack, you’re one photo away from a comprehensive nutritional breakdown in an instant. It’s like having a personal dietitian in your pocket, always ready to help you make smarter food choices with ease and precision.

Additionally, we used the Revised Harris-Benedict Equation to give users an estimate of their suggested daily calories, factoring in their sex, height, weight, and age. This makes the application more personalized and tailored to the user.

# 🛠️ How we built it 💬

By integrating Google Cloud, we aimed to take the guesswork out of calorie counting by using easily available information and integrating the Vision API. Our app is designed to remove barriers, providing a seamless and engaging experience. Just snap a photo, and the rest is taken care of by our intelligent algorithms.

On the front end, we use Python with the CustomTktinter library to create a simple and intuitive user interface. Our features include allowing users to upload or capture photos to be processed, calculating the calories they need in a day, and tracking everything a user eats in a day with a clear bar to represent their calorie goal.

# 🚧 Challenges we ran into ⛔

One of our earliest and most significant hurdles was defining the scope of the AI to handle a diversity of meals. This was the reason we used the Vision API from Google Cloud to process our images. Given the timeframe of this project, we had to limit our ability to easily identifiable food. 

We also worked hard to optimize the app and API calls for speed, as we understand that every second counts when you're hungry. Balancing accuracy with speed was a delicate process that our team navigated with perseverance and creativity.

# 🎉 Accomplishments that we're proud of 🏆

Being a brand-new team to hackathons, we are incredibly proud of what we have achieved in 36 hours. Our journey led us from the intricacies of building a sleek, user-friendly front-end interface with Python's Tkinter to architecting a robust backend powered by the sophistication of the Google Cloud Platform. The culmination of this effort is CalTrack—an integration of technologies that not only embraces but excels at transforming images into actionable nutritional insights.

# 🧠 What we learned 🤓

Building CalTrack has been a rigorous educational experience, packed with valuable lessons at every stage. We ventured into the complex territories of machine learning and user interface design, greatly enhancing our technical skill set. Taking on the Google Cloud Platform, we went from novices to proficient users, tapping into the power of its Vision API, which now serves as the backbone of our app. The learning process was challenging, but we embraced the opportunity to grow and improve, much like adventurers enjoy the ascent and the perspective it brings.

# 🔮 What's next for CalTrack ⏭️

The road ahead for CalTrack includes expanding our food database to cover even more variety, implementing user-friendly features like meal suggestions, and enhancing our AI to provide even more precise nutritional information. 

We're on a mission to make healthy eating hassle-free for everyone, and this is just the beginning.
