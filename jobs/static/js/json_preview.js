document.addEventListener('DOMContentLoaded', function() {
    // Dhyan dein: Agar aapka field CKEditor hai, toh ID change ho sakti hai.
    // Default Textarea ke liye ID 'id_additional_info' ya jo bhi field aapne banayi hai.
    const jsonInput = document.querySelector('textarea'); 
    const previewArea = document.querySelector('#magic-preview');

    if (jsonInput) {
        jsonInput.placeholder = "Yahan apna JSON paste karein...";
        
        jsonInput.addEventListener('input', function() {
            try {
                const data = JSON.parse(jsonInput.value);
                
                // HTML rendering logic
                let htmlContent = `
                    <div style="background: linear-gradient(90deg, #6366f1, #ec4899); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                        <h1 style="color: white; font-size: 20px; margin: 0;">${data.job_title || 'Title missing...'}</h1>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
                        <div style="background: #1e293b; padding: 10px; border-radius: 5px; border-left: 3px solid #22d3ee;">
                            <small style="color: #64748b;">TOTAL POSTS</small><br>
                            <strong>${data.total_posts || 'N/A'}</strong>
                        </div>
                        <div style="background: #1e293b; padding: 10px; border-radius: 5px; border-left: 3px solid #fbbf24;">
                            <small style="color: #64748b;">AGE LIMIT</small><br>
                            <div>${data.age_limit || 'N/A'}</div>
                        </div>
                    </div>

                    <div>${data.category_details || ''}</div>
                    <div>${data.physical_details || ''}</div>
                    
                    <div style="margin-top: 20px; padding: 15px; background: #1e293b; border-radius: 8px;">
                        <h4 style="margin-top: 0;">🔗 Important Links</h4>
                        ${data.important_links || ''}
                    </div>
                `;
                
                previewArea.innerHTML = htmlContent;
                jsonInput.style.borderColor = "#22d3ee";
            } catch (e) {
                previewArea.innerHTML = `<div style="text-align:center; margin-top:50px;">
                    <p style="color: #ef4444; font-size: 18px;">❌ Invalid JSON Format</p>
                    <p style="color: #64748b;">Kripya brackets { } aur commas , check karein.</p>
                </div>`;
                jsonInput.style.borderColor = "#ef4444";
            }
        });
    }
});