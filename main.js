document.addEventListener('DOMContentLoaded', () => {
    // Add dynamic value updating effect on the dashboard inputs
    const inputs = {
        cpu: document.getElementById('cpu'),
        memory: document.getElementById('memory'),
        disk: document.getElementById('disk'),
        db_load: document.getElementById('db_load')
    };

    const displays = {
        cpu: document.getElementById('disp-cpu'),
        memory: document.getElementById('disp-memory'),
        disk: document.getElementById('disp-disk'),
        db_load: document.getElementById('disp-db')
    };

    // Update display values when input changes
    Object.keys(inputs).forEach(key => {
        if (inputs[key] && displays[key]) {
            inputs[key].addEventListener('input', (e) => {
                const val = e.target.value;
                displays[key].textContent = val ? `${val}%` : '--%';
                
                // Add a small animation effect to the display value
                displays[key].style.transform = 'scale(1.1)';
                displays[key].style.color = 'var(--primary-color)';
                
                setTimeout(() => {
                    displays[key].style.transform = 'scale(1)';
                    displays[key].style.color = '';
                }, 200);
            });
        }
    });

    // Form submission animation
    const form = document.getElementById('predict-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            
            btn.innerHTML = '<i class="ph ph-spinner ph-spin"></i> Analyzing...';
            btn.style.opacity = '0.8';
            btn.style.pointerEvents = 'none';
            
            // Allow form to submit normally after a slight delay to show animation
            // In a real SPA we would preventDefault, but here we let Flask handle it
        });
    }
});
