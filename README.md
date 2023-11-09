# DonateMe

Ever felt your $10 holds more value in the right hands? Want to directly fund a neighbor's vivid dream? You're in the right place! DonateMe is where generosity meets community, connecting you with neighbors to make dreams happen!

## MVP Features

The MVP of DonateMe focuses on foundational features that establish a secure, user-centric platform for community support. Here's what we are including in our initial release:

- **User Registration**: Secure signup with phone number verification and GPS location check to ensure community integrity and safety.
  - *Status*: Planned
- **Community Assistance Posts**: Users can create and share their personal stories, set clear financial goals, and provide documentation to foster trust.
  - *Status*: In Progress
- **Search Functionality**: Essential search tools enable users to find assistance posts or donors based on location and other criteria.
  - *Status*: Planned
- **Secure Transactions**: We prioritize the security of all transactions, ensuring that donations are handled with utmost integrity.
  - *Status*: Planned
- **Automated Refunds**: To maintain trust, we ensure that donations are returned if the funding goal isn't met within the set timeframe.
  - *Status*: Planned
- **Follow-up Feedback**: Recipients are required to provide follow-up on how the funds were used, enhancing transparency and donor confidence.
  - *Status*: Planned

We are committed to delivering these key features efficiently to serve our community's needs, with further enhancements planned for future updates.

## Additional Planned Features

As DonateMe evolves, we aim to introduce additional features to enhance the user experience and support our community:

- **User Profiles**: Create and customize your personal profile to share your story with the community.
- **Campaign Creation**: Easily start a campaign for your dream or goal, set a target amount, and a deadline.
- **Local Community Focus**: Find and support campaigns in your local area or state.
- **Social Sharing**: Share campaigns on social media to increase visibility and support.
- **Direct Messaging**: Communicate directly with campaign creators or donors through the platform.

Please note that these features are subject to change as DonateMe evolves. We welcome feedback and contributions from the community!


## Development Process

### User Registration Feature

The user registration feature is a critical component of the DonateMe platform, ensuring that our community is secure and users are verified. Here's how we've implemented this feature:

#### Backend Implementation:

- **User Model**: We've defined a user model in our database with the following fields: `id`, `name`, `email`, `phone_number`, `password_hash`, `location`, `is_phone_verified`, `is_location_verified`, `created_at`, and `updated_at`.
- **Registration Endpoint**: A `/register` endpoint was created to handle the signup process. It validates user input, hashes passwords, and stores user data securely.
- **Phone Number Verification**: Integrated with Twilio API to send an SMS with a verification code. We verify the user's phone number upon code submission.
- **Location Check**: Implemented GPS location check to ensure users are registering within their actual community. This is handled via the frontend and verified on the backend.
- **Security**: Passwords are hashed using bcrypt before storage, and all data is transmitted over HTTPS.

#### Frontend Implementation:

- **Registration Form**: A form was built to capture user information, with HTML5 validation for data integrity.
- **AJAX Calls**: Utilized Axios for AJAX calls to the backend to submit the registration form and handle the phone number verification process.
- **Session Management**: On successful registration and verification, the backend provides a token which is stored in the frontend for session management.
- **User Feedback**: We provide clear messages and prompts to the user throughout the registration process for a seamless user experience.

#### Testing:

- **Unit Tests**: Comprehensive unit tests were written for the backend to ensure the reliability of the registration process.
- **Integration Tests**: Frontend and backend integration is tested to confirm that the entire flow works from end to end.

#### Additional Notes:

- We are considering scalability options for our SMS service to accommodate future growth.
- Data protection and privacy are paramount, and we adhere to the latest regulations in handling user information.

