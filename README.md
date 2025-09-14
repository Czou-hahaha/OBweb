# OBweb - Study in China Website

A modern, responsive website for international students looking to study in China. Built with React, TypeScript, and Tailwind CSS.

## 🌟 Features

- **Modern UI Design**: Clean, responsive design with Tailwind CSS
- **Multi-language Support**: English and Chinese language support
- **University Listings**: Comprehensive database of Chinese universities
- **Program Information**: Detailed program listings with search and filter
- **Service Categories**: 
  - University Selection Consultation
  - Program Guidance Services
- **Interactive Components**: Hover effects, animations, and smooth transitions
- **Mobile Responsive**: Optimized for all device sizes

## 🚀 Live Demo

Visit the live website: [Your Vercel URL will be here]

## 🛠️ Technology Stack

### Frontend
- React 19.1.1
- TypeScript 4.9.5
- Tailwind CSS (Custom implementation)
- React Router DOM 7.9.1
- React i18next for internationalization
- Heroicons for icons

### Backend
- Django 4.2.24
- Django REST Framework
- PostgreSQL (ready for production)

## 📁 Project Structure

```
OBweb/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/           # Page components
│   │   ├── assets/          # Images and static assets
│   │   ├── i18n/           # Internationalization files
│   │   └── App.tsx         # Main application component
│   ├── public/             # Static files
│   └── package.json        # Frontend dependencies
├── backend/                # Django backend API
│   ├── obtest_backend/     # Django project settings
│   ├── universities/       # University management app
│   ├── programs/          # Program management app
│   └── services/          # Service management app
└── docs/                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Node.js 16+ 
- Python 3.9+
- npm or yarn

### Frontend Development
```bash
cd frontend
npm install
npm start
```

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## 🎨 Design Features

- **Color Scheme**: Primary blue (#2563eb) with complementary colors
- **Typography**: Modern, readable fonts with proper hierarchy
- **Animations**: Smooth transitions and hover effects
- **Layout**: Grid-based responsive design
- **Components**: Reusable, accessible UI components

## 📱 Responsive Design

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

## 🌐 Deployment

### Vercel (Frontend)
1. Connect your GitHub repository to Vercel
2. Set build command: `cd frontend && npm run build`
3. Set output directory: `frontend/build`
4. Deploy automatically on every push

### Backend Deployment
- Ready for deployment on platforms like Heroku, Railway, or DigitalOcean
- Environment variables configuration included

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Contact

For questions or support, please contact us through the website contact form.

---

Built with ❤️ for international students pursuing education in China.
