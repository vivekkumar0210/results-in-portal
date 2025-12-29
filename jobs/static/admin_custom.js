document.addEventListener('DOMContentLoaded', function() {
    const mappings = [
        { check: 'id_show_in_latest_job', field: '.field-job_title' },
        { check: 'id_show_in_result', field: '.field-result_title' },
        { check: 'id_show_in_admit_card', field: '.field-admit_title' },
        { check: 'id_has_physical_standards', field: '.field-physical_details' },
        { check: 'id_has_selection_mode', field: '.field-selection_mode' }
    ];

    mappings.forEach(item => {
        const checkbox = document.getElementById(item.check);
        const fieldRow = document.querySelector(item.field);

        function toggle() {
            if (checkbox && fieldRow) {
                fieldRow.style.display = checkbox.checked ? 'block' : 'none';
            }
        }

        if (checkbox) {
            checkbox.addEventListener('change', toggle);
            toggle(); 
        }
    });
});